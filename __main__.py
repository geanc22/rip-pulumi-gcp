"""A Google Cloud Python Pulumi program"""

import pulumi
from config import bucket_config
from config import bucket2_config #, artifact_registry_config
from components.buckets.basic_bucket import StorageBucket
from components.buckets.storage_bucket import StorageBucket2
from components.artifact_registry.artifact_registry import ArtifactRegistry
#from components.buckets.storage_bucket import StorageBucket

# Crear Buckets usando la configuración
##public_bucket = StorageBucket(bucket_config["public_bucket_name"], public=True, location=bucket_config["location"])
##private_bucket = StorageBucket(bucket_config["private_bucket_name"], public=False, location=bucket_config["location"])

private_bucket = StorageBucket(
    bucket_config["private_bucket_name"], 
    location=bucket_config["location"]
)

bucket = StorageBucket2(
    name="my-bucket",
    project_id=bucket2_config["project_id"],
    env=bucket2_config["env"],
    account=bucket2_config["account"],
    location=bucket2_config["location"],
    force_destroy=bucket2_config["force_destroy"],
    origin=bucket2_config["origin"],
    target=bucket2_config["target"],
)

#--- Crear el repositorio en Artifact Registry (en construccion)----#
# artifact_repo = ArtifactRegistry(
#     name=artifact_registry_config["name"],
#     project_id=artifact_registry_config["project_id"],
#     location=artifact_registry_config["location"],
#     format=artifact_registry_config["format"],
#     description=artifact_registry_config["description"],
# )


#--- Exportar los nombres de los buckets
##pulumi.export("public_bucket_name", public_bucket.bucket_name)
pulumi.export("private_bucket_name", private_bucket.bucket_name)
pulumi.export("bucket_name", bucket)

##--- Exportar el nombre del repositorio
#pulumi.export("artifact_repo_name", artifact_repo.repo_name)