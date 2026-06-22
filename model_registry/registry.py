"""Model registry with versioning."""
class Registry:
    def __init__(self, backend="mlruns/"):
        self.backend = backend
        self.models = {}
        
    def register(self, name, model, metrics=None):
        if name not in self.models:
            self.models[name] = []
        self.models[name].append({"model": model, "metrics": metrics or {}, "stage": "development"})
        
    def promote(self, name, version, stage="staging"):
        if name in self.models and version <= len(self.models[name]):
            self.models[name][version-1]["stage"] = stage
            
    def rollback(self, name, version):
        self.promote(name, version, "production")
        
    def list_versions(self, name):
        return self.models.get(name, [])
