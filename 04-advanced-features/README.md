# 04. Advanced Features

This module covers several advanced capabilities of GitHub Actions. Each topic is demonstrated by a workflow in [`.github/workflows`](../.github/workflows) whose file name begins with `04-advanced-features--`.

## Topics & Workflows

- **Runner Types** – [`04-advanced-features--01-runner-types.yaml`](../.github/workflows/04-advanced-features--01-runner-types.yaml)
  - shows GitHub-hosted Linux/Windows/macOS runners, container jobs, and a third-party runner
- **Artifacts** – [`04-advanced-features--02-artifacts.yaml`](../.github/workflows/04-advanced-features--02-artifacts.yaml)
  - one job uploads a text file and a second job downloads and displays it
- **Caching** – [`04-advanced-features--03-caching.yaml`](../.github/workflows/04-advanced-features--03-caching.yaml)
  - demonstrates the `actions/cache` action and `setup-node` built‑in caching
- **GitHub Permissions** – [`04-advanced-features--04-github-permissions.yaml`](../.github/workflows/04-advanced-features--04-github-permissions.yaml)
  - compares read-only vs read/write `GITHUB_TOKEN` permissions on pull requests
- **Third-Party Authentication** – [`04-advanced-features--05-third-party-auth.yaml`](../.github/workflows/04-advanced-features--05-third-party-auth.yaml)
  - contrasts static AWS credentials with OIDC-based authentication
- **Matrix & Conditionals** – [`04-advanced-features--06-matrix-and-conditionals.yaml`](../.github/workflows/04-advanced-features--06-matrix-and-conditionals.yaml)
  - runs a job across a two-dimensional matrix and skips steps based on conditions
- **Dynamic Matrix** – [`04-advanced-features--07-dynamic-matrix.yaml`](../.github/workflows/04-advanced-features--07-dynamic-matrix.yaml)
  - generates a dynamic set of jobs to be run using the matrix strategy
- **Workflow Commands**
[`04-advanced-features--08-workflow-commands.yaml`](../.github/workflows/04-advanced-features--08-workflow-commands.yaml)
  - demonstrates specially formatted instructions that enable communication with the Github Action runner to control the workflow's behavior

The caching example also includes a minimal Node project in [`caching/minimal-node-project`](./caching/minimal-node-project).