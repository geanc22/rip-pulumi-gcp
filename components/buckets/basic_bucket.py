import pulumi
from pulumi_gcp import storage

class StorageBucket(pulumi.ComponentResource):
    def __init__(self, name: str, location: str, opts=None):
    #def __init__(self, name: str, public: bool, location: str, opts=None):
        super().__init__("custom:resource:StorageBucket", name, {}, opts)

        # Crear el bucket
        bucket = storage.Bucket(
            
            name,   #pulumi aleatoriamente designa al final del name desginado 
            
            
            location=location,
            uniform_bucket_level_access=True,
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
