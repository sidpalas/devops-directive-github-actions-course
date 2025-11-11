# 02. Why GitHub Actions


![](./readme-assets/developer-surveys.png)

GitHub Actions is one of the most popular CI tools across the industry. Here is a comparison with some of the other top choices:

| Tool        | Why Yes?                                                                                                                                             | Why No?                                                                                                                |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| GitHub Actions | • Your code is (likely) on GitHub already  <br> • Minimal barrier to entry <br> • Expansive public marketplace <br> • Market leadership leads to improved tooling (like [namespace.so](https://namespace.so)!) | • If you aren’t already using GitHub <br> • Less powerful pipeline reuse primitives <br> • Painful debugging experience <br> • Limited analytics/observability |
| GitLab CI   | • Your code (might be) on GitLab already <br> • Minimal barrier to entry (if using GitLab) <br> • Deep integration with other GitLab features <br> • GitLab “Auto DevOps” | • If you aren’t already using GitLab <br> • Smaller public marketplace (<500 total)                                       |
| CircleCI    | • Your code isn’t on GitHub or GitLab (CircleCI is VCS agnostic) <br> • Built-in “retry with SSH” feature is 🔥                                            | • Requires initial setup (vs. GHA + GitLab) <br> • Smaller public orbs marketplace (3653 total)                           |
| Jenkins     | • You (might) already be using it <br> • The plugin ecosystem is vast                                                                                      | • Incurs significant maintenance overhead (security and plugin dependencies) <br> • Groovy pipeline DSL feels outdated    |
