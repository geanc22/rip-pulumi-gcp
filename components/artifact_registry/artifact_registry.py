import pulumi
from pulumi_gcp import artifactregistry

class ArtifactRegistry(pulumi.ComponentResource):
    def __init__(self, name: str, project_id: str, location: str, format: str, description: str, opts=None):
        super().__init__("custom:resource:ArtifactRegistry", name, {}, opts)

        # Crear el repositorio de Artifact Registry
        repo = artifactregistry.Repository(
            name,
            project=project_id,
            location=location,
            format=format,
            description=description,
        )

        # Exportar el nombre del repositorio
        self.repo_name = repo.name
        self.register_outputs({"repo_name": self.repo_name})
