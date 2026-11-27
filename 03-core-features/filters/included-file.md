# Path Filter Demo: Included File

## Purpose
This `.md` file demonstrates GitHub Actions **path filters**.

## How it works
The workflow [03-core-features--04-triggers-and-filters.yaml](../.github/workflows/03-core-features--04-triggers-and-filters.yaml) triggers on `pull_request` events when:

```
paths:
  - '03-core-features/filters/*.md'     # ✅ Includes this file
  - '!03-core-features/filters/*.txt'   # ❌ Excludes excluded-file.txt
```

**Commit changes to this file** → Workflow triggers on PR.

**See also:** [Core Features Overview](../README.md)

---
*Example file for GitHub Actions learning repo.*

