# Included File

This file is used to demonstrate **path filters** in GitHub Actions workflows.

Modifying this file will trigger workflows that include `filters/included-file.md` in their path filter, unlike `excluded-file.txt` which is ignored.

## Example Usage

```yaml
on:
  push:
    paths:
      - 'filters/**.md'
```

## How Path Filters Work

GitHub Actions supports two path filter keys:

- **`paths`** — triggers the workflow when a matching file is changed.
- **`paths-ignore`** — skips the workflow when only matching files are changed.

You can also use negation patterns to fine-tune behavior:

```yaml
on:
  push:
    paths:
      - '**.md'
      - '!**/excluded-file.txt'
```

## Notes

- Glob patterns follow the same syntax as `.gitignore`.
- At least one changed file must match for the workflow to trigger.
- `paths` and `paths-ignore` cannot be used together in the same event trigger.
