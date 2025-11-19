# Common workflows

## Validate
- **Lint** – Run automated linters (e.g., ESLint, flake8) to catch style violations and obvious syntax errors early.
- **Test** – Execute unit, integration, or end-to-end test suites to verify that new changes don’t break existing functionality.
- **Static analysis** – Analyze source code without running it to uncover bugs, complexity hot-spots, or security issues.
  - **Security scanning** – Check code and dependencies for known vulnerabilities or insecure patterns.
  - **Code quality** – Measure metrics such as complexity, duplication, and coverage to enforce quality gates.

## Build
- **Compile** – Transform source code into executable binaries or bytecode (e.g., `go build`, `javac`).
- **Package (container, AMI, etc.)** – Assemble and version distributable artifacts like Docker images, OS packages, or Amazon Machine Images.

## Deploy
- **Push based** – CI workflow pushes artifacts or infrastructure changes directly to the target environment (e.g., `kubectl apply`, `terraform apply`).
- **Pull based (GitOps)** – Commit the desired state to a Git repo; an agent running in the environment detects the change and pulls it in.

## Other Automation
- **Release automation** – Automatically tag versions, generate release notes, and publish artifacts when code is merged to a release branch.
- **Stale issues/PRs** – Mark or close inactive issues and pull requests after a period of inactivity to keep the backlog manageable.
- **Dependency upgrades** – Periodically open PRs that bump third-party libraries or container images to the latest safe versions.