import pulumi

config = pulumi.Config()

##----Configuración de Buckets-----#
bucket_config = {
    #"public_bucket_name": config.require("publicBucketName"),
    "private_bucket_name": config.require("privateBucketName"),
    "location": config.get("bucketLocation") or "southamerica-west1",
}

bucket2_config = {
    # Leer variables de configuración desde Pulumi.dev.yaml (o el stack activo)
    "project_id" : config.require("project_id"),
    "env" : config.require("env"),
    "account" : config.require("account"),
    "location" : config.require("location"),
    "force_destroy" : config.get_bool("force_destroy"),  # get_bool convierte "true"/"false" en bool
    "origin" : config.require("origin"),
    "target" : config.require("target")
}

###----Configuración del Artifact Registry (en construccion)---#
# artifact_registry_config = {
#     "name": config.require("artifact_registry.name"),
#     "project_id": config.require("project_id"),
    
#     "location": config.require("location"),
#     "format": config.require("artifact_registry.format"),
#     "description": config.get("artifact_registry.description") or "Repositorio de artifacts",
    
# }



##-----Configuración de Compute Engine (en contruccion)---#
# compute_config = {
#     "vm_name": config.require("vmName"),
#     "vm_machine_type": config.get("vmMachineType") or "e2-medium",
#     "vm_zone": config.get("vmZone") or "us-central1-a",
#     "vm_disk_size": config.get_int("vmDiskSize") or 50,
#     "vm_image": config.get("vmImage") or "debian-cloud/debian-11",
# }
