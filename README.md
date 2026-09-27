# Privacy PT Coach

An open-source, privacy-first physical-therapy coaching prototype that uses on-device computer vision to analyze movement and provide real-time exercise feedback without requiring raw camera video to leave the user's device.

> **Status:** pre-alpha / active build. This is a research and developer project, not a medical device and not a substitute for professional medical care.

## Why this project

Many movement-coaching systems depend on cloud video processing. For physical-therapy-style exercises, that can mean sending highly personal footage off-device.

Privacy PT Coach explores a different architecture:

- camera frames processed locally
- pose landmarks and motion features computed on-device
- no raw video upload required for the core workflow
- optional wearable sensor fusion where platform APIs allow it
- transparent, reproducible performance benchmarks across hardware

The immediate goal is a working local demo that can recognize a small set of exercises, count repetitions, measure motion quality, and provide simple real-time cues.

## Planned MVP

1. Capture webcam / phone-camera video.
2. Run local pose estimation.
3. Track joint angles and temporal motion features.
4. Detect exercise phase and repetitions.
5. Generate simple rule-based feedback.
6. Store only user-approved derived metrics locally.
7. Benchmark latency, throughput, power use, and memory footprint.

## Architecture

```text
Camera
  |
  v
Local frame capture
  |
  v
Pose estimation
  |
  v
Landmarks + temporal features
  |
  +------> Optional wearable / IMU adapter
  |
  v
Exercise state machine
  |
  v
Quality metrics + feedback rules
  |
  v
Local UI / session summary
```

See [Architecture](docs/ARCHITECTURE.md) for the proposed component design.

## Hardware strategy

The project is intentionally cross-platform. The benchmark plan will compare:

- CPU-only baseline
- Apple Silicon
- NVIDIA CUDA / TensorRT
- AMD GPU / ROCm where supported
- edge devices such as Jetson-class hardware

See [Hardware](docs/HARDWARE.md) and [Benchmark Plan](docs/BENCHMARKS.md).

## Privacy principles

- Local-first inference.
- Raw video is not required to leave the device.
- Data retention should be explicit and user-controlled.
- Derived metrics should be separable from identifiable video.
- Network activity should be auditable.
- No medical diagnosis claims.

## Roadmap

The near-term path is:

- **v0.1:** local camera + pose-estimation demo
- **v0.2:** repetition counting and exercise state machine
- **v0.3:** quality metrics and local session summaries
- **v0.4:** optional wearable sensor experiments
- **v0.5:** cross-hardware benchmark report

Full roadmap: [docs/ROADMAP.md](docs/ROADMAP.md)

## Open development

The project will be developed publicly. Reproducibility matters: setup steps, benchmark methodology, hardware configuration, limitations, and failed experiments should be documented rather than hidden.

Contributions will be welcome once the initial scaffold and baseline implementation land.

## Hardware support / sponsorship

I am looking for hardware partners willing to provide a **development unit, loaner, refurbished system, cloud credits, or developer discount** so the project can publish reproducible local-inference benchmarks.

Useful targets include:

- NVIDIA RTX-class GPUs and CUDA/TensorRT-capable systems
- AMD Radeon / Ryzen AI development systems
- compact AI workstations and mini PCs
- edge AI devices
- high-memory systems useful for local vision and multimodal experiments

This is not a request for cash. Hardware access is more useful because the output can be a public implementation and benchmark record.

See [SPONSORSHIP.md](SPONSORSHIP.md) for details.

## License

MIT. See [LICENSE](LICENSE).

## Maintainer

Viswanath Chilakala  
GitHub: [@viswamba](https://github.com/viswamba)
