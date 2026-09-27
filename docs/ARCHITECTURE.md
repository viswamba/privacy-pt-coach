# Architecture

## Design goals

The system should be local-first, modular, benchmarkable, and easy to run on commodity hardware.

## Proposed pipeline

### 1. Capture layer
Accept webcam, prerecorded test clips, and later mobile-camera streams. The capture layer should expose timestamps and frame metadata without coupling the rest of the system to a specific camera API.

### 2. Pose-estimation backend
A backend interface will allow different runtimes and models to be swapped without rewriting the application.

Candidate backends may include ONNX Runtime, TensorRT, Core ML, ROCm-compatible runtimes, and CPU baselines.

### 3. Feature extraction
Convert pose landmarks into higher-level signals such as:

- joint angles
- angular velocity
- range of motion
- left/right symmetry
- temporal smoothness
- exercise phase

### 4. Exercise state machine
Each exercise gets a transparent state machine rather than an opaque end-to-end classifier for the initial MVP.

Example:

```text
START -> ECCENTRIC -> BOTTOM -> CONCENTRIC -> COMPLETE
```

This makes rep counting and feedback easier to inspect and debug.

### 5. Feedback engine
The first implementation should use deterministic rules derived from the extracted features. The system should explain which metric triggered a cue.

### 6. Optional sensor-fusion adapter
Wearable / IMU data should be treated as optional. Camera-only operation must remain functional. Platform API availability and sensor-access limitations will be documented experimentally.

### 7. Local session store
Default storage should contain derived metrics rather than raw frames. Raw-video retention, if ever enabled for debugging, should be explicit and opt-in.

## Privacy boundary

The default architecture should not require a cloud inference endpoint.

```text
DEVICE BOUNDARY
+-------------------------------------------+
| Camera -> inference -> metrics -> UI      |
|                 |                         |
|                 +-> local session store   |
+-------------------------------------------+
             |
             +---- optional user-triggered export
```

## Initial technology direction

The first baseline should prioritize portability and developer speed:

- Python
- OpenCV or equivalent capture layer
- ONNX-compatible pose model where practical
- modular inference backend abstraction
- simple local UI
- JSON/CSV benchmark output

Optimization-specific paths can then be added for CUDA/TensorRT, Apple Silicon, and AMD runtimes.

## Non-goals for the MVP

- diagnosis
- treatment recommendations
- autonomous clinical decision-making
- cloud account system
- social features
- collection of large amounts of user video
