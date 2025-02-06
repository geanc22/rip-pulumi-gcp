import pulumi
from pulumi_gcp import storage

class StorageBucket2(pulumi.ComponentResource):
    #def __init__(self, name: str, location: str, opts=None):
    #def __init__(self, name: str, public: bool, location: str, opts=None):
    def __init__(self, name: str, project_id: str, env: str, account: str, location: str, force_destroy: bool, origin: str, target: str, opts=None):
        super().__init__("custom:resource:StorageBucket", name, {}, opts)

        bucket_name = f"{account}-{env}-{name}"

        # Crear el bucket
        bucket = storage.Bucket(
            resource_name=name,
            #name,   #pulumi aleatoriamente designa al final del name desginado 
            #bucket_name
            name=bucket_name,
            location=location,
            force_destroy=force_destroy,
            labels={
                "project_id": project_id,
                "origin": origin,
                "target": target,
            },
            uniform_bucket_level_access=True
        )

        # # Si es público, asignar permisos
        # if public:
        #     storage.BucketIAMBinding(
        #         f"{name}-public-access",
        #         bucket=bucket.name,
        #         role="roles/storage.objectViewer",
        #         members=["allUsers"],
        #     )

        # Exportar el nombre del bucket
        self.bucket_name = bucket.name
        self.register_outputs({"bucket_name": self.bucket_name})
