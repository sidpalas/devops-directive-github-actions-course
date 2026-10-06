# 06. Authoring Actions

This module demonstrates how to build custom GitHub Actions and reusable workflows. Each example below has a workflow located in `.github/workflows/` following the pattern `06-authoring-actions--<name>.yaml`.

## Composite Action
- **Folder:** `composite-action`
- **Workflow:** [`.github/workflows/06-authoring-actions--01-composite-action.yaml`](../.github/workflows/06-authoring-actions--01-composite-action.yaml)
- **What it does:** defines a simple action that prints a greeting and outputs a
  random number. The workflow demonstrates calling the action twice in
  separate jobs.

## Reusable Workflows
- **Folder:** `reuseable-workflow`
- **Workflows:**
 - [`.github/workflows/06-authoring-actions--02-reuseable-workflows-source.yaml`](../.github/workflows/06-authoring-actions--02-reuseable-workflows-source.yaml) – defines the reusable workflow
 - [`.github/workflows/06-authoring-actions--03-reuseable-workflows-caller.yaml`](../.github/workflows/06-authoring-actions--03-reuseable-workflows-caller.yaml) – calls the reusable workflow
  - **What they do:** the source workflow exposes inputs and secrets and prints
    them in a job. The caller workflow triggers manually and invokes the source
    workflow using both a relative path and a specific commit reference.

## JavaScript & TypeScript Actions
- **Folder:** `javascript-actions`
- **Workflow:** [`.github/workflows/06-authoring-actions--04-javascript-actions.yaml`](../.github/workflows/06-authoring-actions--04-javascript-actions.yaml)
- **What it does:** runs three jobs showcasing different approaches for
  JavaScript/TypeScript actions:
  - `javascript-action-no-build` uses vanilla Node with dependencies committed.
  - `javascript-action-with-build` demonstrates a Node action that normally
    would require a build step (pulled in as a submodule).
  - `typescript-action-with-build` shows a TypeScript action compiled before
    execution.

## Container Actions
- **Folder:** `container-actions`
- **Workflow:** [`.github/workflows/06-authoring-actions--05-container-actions.yaml`](../.github/workflows/06-authoring-actions--05-container-actions.yaml)
- **What it does:** runs three jobs that execute container-based actions:
  - `shell-dockerfile` builds a shell-based container action from a local
    Dockerfile each run.
  - `shell-public-container-image` reuses a prebuilt container image to skip the
    build step.
  - `python-dockerfile` builds and runs a Python action defined by a Dockerfile
    and prints a greeting.