# Hardware

## Philosophy

This project should not depend on one expensive accelerator. A CPU baseline establishes accessibility; accelerated backends establish the performance ceiling.

## Target tiers

### Tier 0 — CPU baseline
Any recent x86-64 or Apple Silicon machine capable of running the reference pipeline.

Purpose: correctness, accessibility, and a common comparison point.

### Tier 1 — Integrated / compact systems
Apple Silicon, Ryzen AI-class systems, and other integrated accelerators.

Purpose: evaluate quiet, low-power local inference.

### Tier 2 — Discrete GPU workstation
Primary development target for high-performance experimentation.

Desired characteristics:

- 12 GB+ accelerator memory preferred
- modern inference-runtime support
- DisplayPort / HDMI output for local demo development
- sufficient system RAM for model conversion and profiling

### Tier 3 — Edge AI
Jetson-class and comparable devices.

Purpose: evaluate deployment where low power and small footprint matter more than peak throughput.

## Hardware currently useful to the project

Hardware partners can contribute any of the following:

- development units
- loaner hardware
- refurbished systems
- previous-generation professional GPUs
- cloud GPU credits
- developer discounts

The benchmark report will identify the exact model, software stack, power mode, model precision, input resolution, and measurement method.

## What matters more than retail value

A discontinued or previous-generation device can still be useful if it enables a distinct runtime, memory tier, or power envelope to be measured.
