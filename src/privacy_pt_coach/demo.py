"""Local webcam pose demo for Privacy PT Coach.

The default path processes frames locally, displays pose landmarks and basic
movement metrics, and does not save or upload camera frames.
"""

from __future__ import annotations

import argparse
import time
from collections import deque
from dataclasses import dataclass

import cv2
import mediapipe as mp

from privacy_pt_coach.geometry import angle_degrees


@dataclass
class RuntimeMetrics:
    fps: float = 0.0
    inference_ms: float = 0.0


class FpsMeter:
    """Rolling FPS estimate that is less jumpy than frame-to-frame FPS."""

    def __init__(self, window: int = 30) -> None:
        self._timestamps: deque[float] = deque(maxlen=max(2, window))

    def update(self, now: float) -> float:
        self._timestamps.append(now)
        if len(self._timestamps) < 2:
            return 0.0

        elapsed = self._timestamps[-1] - self._timestamps[0]
        if elapsed <= 0:
            return 0.0

        return (len(self._timestamps) - 1) / elapsed


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Privacy PT Coach's local webcam pose demo."
    )
    parser.add_argument("--camera", type=int, default=0, help="Camera index.")
    parser.add_argument("--width", type=int, default=1280, help="Requested width.")
    parser.add_argument("--height", type=int, default=720, help="Requested height.")
    parser.add_argument(
        "--model-complexity",
        type=int,
        choices=(0, 1, 2),
        default=1,
        help="MediaPipe pose model complexity.",
    )
    parser.add_argument(
        "--no-mirror",
        action="store_true",
        help="Do not mirror the webcam preview.",
    )
    return parser.parse_args()


def _visible_joint_angle(
    landmarks,
    first_index: int,
    middle_index: int,
    last_index: int,
    min_visibility: float = 0.5,
) -> float | None:
    points = [
        landmarks[first_index],
        landmarks[middle_index],
        landmarks[last_index],
    ]
    if any(point.visibility < min_visibility for point in points):
        return None

    return angle_degrees(
        (points[0].x, points[0].y),
        (points[1].x, points[1].y),
        (points[2].x, points[2].y),
    )


def _draw_hud(
    frame,
    metrics: RuntimeMetrics,
    detected: bool,
    left_knee: float | None,
    right_knee: float | None,
) -> None:
    lines = [
        "Privacy PT Coach | LOCAL-ONLY DEMO",
        f"Pose: {'detected' if detected else 'not detected'}",
        f"FPS: {metrics.fps:5.1f} | inference: {metrics.inference_ms:5.1f} ms",
        (
            "2D knee angle L/R: "
            f"{left_knee:5.1f} / {right_knee:5.1f} deg"
            if left_knee is not None and right_knee is not None
            else "2D knee angle L/R: --"
        ),
        "Q or Esc: quit",
    ]

    x, y = 18, 30
    for line in lines:
        cv2.putText(
            frame,
            line,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )
        cv2.putText(
            frame,
            line,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (25, 25, 25),
            1,
            cv2.LINE_AA,
        )
        y += 28


def main() -> None:
    args = _parse_args()

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    camera = cv2.VideoCapture(args.camera)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

    if not camera.isOpened():
        raise SystemExit(
            f"Could not open camera {args.camera}. "
            "Check camera permissions or try --camera 1."
        )

    fps_meter = FpsMeter()
    metrics = RuntimeMetrics()

    try:
        with mp_pose.Pose(
            static_image_mode=False,
            model_complexity=args.model_complexity,
            enable_segmentation=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        ) as pose:
            while True:
                ok, frame = camera.read()
                if not ok:
                    raise RuntimeError("Camera stopped returning frames.")

                if not args.no_mirror:
                    frame = cv2.flip(frame, 1)

                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb.flags.writeable = False

                started = time.perf_counter()
                result = pose.process(rgb)
                metrics.inference_ms = (time.perf_counter() - started) * 1000.0
                metrics.fps = fps_meter.update(time.perf_counter())

                left_knee = None
                right_knee = None
                detected = result.pose_landmarks is not None

                if detected:
                    landmarks = result.pose_landmarks.landmark
                    left_knee = _visible_joint_angle(
                        landmarks,
                        mp_pose.PoseLandmark.LEFT_HIP.value,
                        mp_pose.PoseLandmark.LEFT_KNEE.value,
                        mp_pose.PoseLandmark.LEFT_ANKLE.value,
                    )
                    right_knee = _visible_joint_angle(
                        landmarks,
                        mp_pose.PoseLandmark.RIGHT_HIP.value,
                        mp_pose.PoseLandmark.RIGHT_KNEE.value,
                        mp_pose.PoseLandmark.RIGHT_ANKLE.value,
                    )

                    mp_drawing.draw_landmarks(
                        frame,
                        result.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS,
                    )

                _draw_hud(frame, metrics, detected, left_knee, right_knee)
                cv2.imshow("Privacy PT Coach - local pose demo", frame)

                key = cv2.waitKey(1) & 0xFF
                if key in (ord("q"), 27):
                    break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
