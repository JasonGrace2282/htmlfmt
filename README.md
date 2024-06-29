# htmlfmt
Format HTML with `pre-commit`!


## Usage
Add the following to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/JasonGrace2282/htmlfmt
  rev: v0.1.0
  hooks:
    - id: htmlfmt
      files: ^.*\.html$
```
