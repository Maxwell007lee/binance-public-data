# CI/CD Rules

1. Pull requests must pass contract tests before merge.
2. Linting (`ruff`) and type checking (`python -m compileall`) must pass.
3. Any state-machine YAML change requires matching contract-test updates.
4. Any schema change requires:
   - version bump in schema package,
   - compatibility review,
   - replay validation.
5. Default deployment policy is **manual approval** after CI success.
6. Production release requires evidence bundle retention and immutable build artifacts.
7. No service may be deployed if hard-gate enforcement is disabled.
