# Roadmap

## Phase 0 — Scaffold

- repository structure
- architecture notes
- privacy requirements
- benchmark methodology
- hardware matrix

## Phase 1 — Local pose demo

Goal: camera input to pose landmarks fully on-device.

Deliverables:

- webcam capture
- one baseline pose model
- live overlay
- FPS and latency instrumentation
- CPU baseline results

## Phase 2 — Exercise state machine

Goal: reliably identify phases and repetitions for a small exercise set.

Initial candidates:

- squat
- shoulder abduction
- sit-to-stand
- controlled knee extension

Deliverables:

- feature extraction
- rep counter
- phase/state visualization
- deterministic tests using prerecorded clips

## Phase 3 — Quality metrics

Goal: produce understandable movement metrics rather than a black-box score.

Possible metrics:

- range of motion
- tempo
- symmetry
- path consistency
- pause duration
- compensatory motion proxies

## Phase 4 — Hardware acceleration

- NVIDIA CUDA / TensorRT path
- Apple Silicon path
- AMD path where runtime support permits
- edge-device experiments
- reproducible benchmark report

## Phase 5 — Optional sensor fusion

Investigate whether wearable motion signals add meaningful information beyond camera-only tracking.

The camera-only experience remains the required baseline.

## Phase 6 — Demo-quality application

- clean local UI
- session history
- exportable summary
- privacy controls
- documented installer / environment setup

## Success criteria

The project is successful when another developer can clone it, run the same benchmark, reproduce the methodology, and understand exactly what data leaves the device.
