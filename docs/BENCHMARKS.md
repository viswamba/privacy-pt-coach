# Benchmark Plan

## Objective

Publish reproducible measurements for local pose-inference workloads across multiple hardware classes.

## Core metrics

- end-to-end frame latency
- inference latency
- sustained FPS
- p50 / p95 latency
- accelerator memory use
- system memory use
- model load time
- power draw where measurable
- thermally sustained performance

## Test controls

Each result should record:

- hardware model
- OS and version
- driver / runtime version
- model name and revision
- precision
- input resolution
- batch size
- warm-up procedure
- benchmark duration
- power mode
- whether rendering is enabled

## Benchmark modes

### Inference-only
Preloaded frames; isolates model/runtime performance.

### End-to-end
Camera capture through landmark output.

### Application
Full pipeline including feature extraction, state machine, and UI.

## Reporting

Results should be machine-readable as CSV or JSON and summarized in Markdown.

No benchmark should be described as a universal hardware ranking. Results apply to the tested model, runtime, configuration, and workload.
