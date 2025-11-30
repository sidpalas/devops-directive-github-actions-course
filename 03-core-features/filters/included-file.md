This change will trigger a workflow run based on these path filters:

```yaml
paths:
  # include markdown files
  - "03-core-features/filters/*.md"
  # Exclude txt files
  - "!03-core-features/filters/*.txt"
```
