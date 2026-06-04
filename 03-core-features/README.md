# 03. Core Features

This module demonstrates the building blocks used in all GitHub Actions workflows. Each example workflow is located in `.github/workflows/` and follows the naming pattern `03-core-features--<name>.yaml`.

## Included Workflows

- [**03-core-features--01-hello-world.yaml**](../.github/workflows/03-core-features--01-hello-world.yaml) – the most basic workflow that prints a message from an inline bash step.
- [**03-core-features--02-step-types.yaml**](../.github/workflows/03-core-features--02-step-types.yaml) – shows different step types including bash, Python, and an action from the marketplace.
- [**03-core-features--03-workflows-jobs-steps.yaml**](../.github/workflows/03-core-features--03-workflows-jobs-steps.yaml) – illustrates how workflows are organised into jobs and steps and how jobs can run in parallel or depend on each other.
- [**03-core-features--04-triggers-and-filters.yaml**](../.github/workflows/03-core-features--04-triggers-and-filters.yaml) – explores triggering events and path filters. This workflow watches changes inside [`03-core-features/filters`](./filters/).
- [**03-core-features--05-environment-variables.yaml**](../.github/workflows/03-core-features--05-environment-variables.yaml) – explains variable scoping at workflow, job and step level.
- [**03-core-features--06-passing-data.yaml**](../.github/workflows/03-core-features--06-passing-data.yaml) – passes data between jobs using job outputs and environment variables.
- [**03-core-features--07-secrets-and-variables.yaml**](../.github/workflows/03-core-features--07-secrets-and-variables.yaml) – demonstrates injecting secrets and variables from both the repository and environments.

See the `filters` directory for sample files that are used by the triggers and filters workflow.