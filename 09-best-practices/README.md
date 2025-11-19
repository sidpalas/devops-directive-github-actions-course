# Best Practices

## Performance

1. **Measure performance** - Establish a baseline first. Capture job duration, queue time, cache hit rate, and any user-visible latency.
2. **Wait less**
   - *Minimize runner queuing* - Ensure sufficient runner capacity to avoid wasted time.
   - *Fail fast* - Group quick pre-checks (lint, type-check) early so broken PRs are rejected ASAP.
3. **Do less**
   - *Conditional filters* - Use `if:` expressions and path filters so only jobs affected by a change run.
   - *Caching* - Re-use dependency installs (`actions/cache`) and compiled layers (`docker/build-push-action`) to avoid redundant work.
4. **Improve resource usage**
   - *Parallelize (cores + jobs)* - Split test matrices by OS/language version; leverage job-level `strategy.matrix` and ensure your tests are utilizing all available CPU cores.
   - *Avoid emulation* - Native ARM and x86 runners beat emulators (e.g., skip QEMU where possible)
5. **Prevent slowdowns** - Track long-tail job times, set alerts when they regress, and prune unused caches/artifacts to keep runtimes predictable.

## Maintainability

1. **Mono- vs. multi-repo considerations** - Think through how you will share logic across projects to avoid copy-pasting and maintining many copies of similar logic.
2. **Define a “CI API” for each service**
   - *Single task runner/build tool* - Tools like **Task**, **Make**, or **Bazel** hide implementation details so workflows simply call `task test`.
   - *Standard commands* - Adopt a common contract (`install`, `test`, `build`, `dev`) so every repo behaves the same on local machines and in CI.
3. **Avoid duplication** - Extract shared steps into **Composite Actions** or **Reusable Workflows** (`.github/workflows/reusable.yml`) and version them just like libraries.
4. **Iterate locally** - Use [`act`](https://github.com/nektos/act) and local scripts to dry-run jobs before pushing, shortening the feedback loop.

## Security

1. **Grant the minimum necessary permissions** - Limit workflow tokens with `permissions:` and job-level `env:`; prefer `GITHUB_TOKEN` over personal tokens.
2. **Avoid long-lived credentials** - Use OpenID Connect (OIDC) to request short-lived cloud creds at job runtime instead of storing secrets.
3. **Pin action versions with the SHA** - Reference actions using the commit SHA (e.g., `@<sha>`), to prevent unexpected updates and potential security issues.
4. **Don’t allow self-hosted runners on fork PRs** - Restrict forked PRs to GitHub-hosted runners to mitigate supply-chain attacks.
5. **Require approval for protected environments** - Tie production deploys to an *Environment* with `required_reviewers`; manual approval gates stop compromised branches from auto-shipping.