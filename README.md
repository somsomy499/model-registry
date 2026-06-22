# Model Registry 📦

MLflow-compatible model registry with versioning, staging, and A/B testing.

## Features

- **Version Control**: Git-like versioning for models
- **Staging Pipeline**: Development → Staging → Production
- **Rollback**: One-click rollback to any previous version
- **A/B Testing**: Traffic splitting between model versions
- **Audit Log**: Complete history of all changes

## Quick Start

```python
from model_registry import Registry

registry = Registry("mlruns/")
registry.register("my-model", model, metrics={"accuracy": 0.94})
registry.promote("my-model", version=1, stage="production")
```

## License

MIT