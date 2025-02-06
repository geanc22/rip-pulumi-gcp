import pulumi
from pulumi_gcp import compute

class ComputeInstance(pulumi.ComponentResource):
    def __init__(self, name: str, machine_type: str, zone: str, disk_size: int, image: str, opts=None):
        super().__init__("custom:resource:ComputeInstance", name, {}, opts)

        # Crear el disco de la VM
        disk = compute.Disk(
            f"{name}-disk",
            size=disk_size,
            zone=zone,
        )

        # Crear la instancia de Compute Engine
        instance = compute.Instance(
            name,
            machine_type=machine_type,
            zone=zone,
            boot_disk=compute.InstanceBootDisk(
                initialize_params=compute.InstanceBootDiskInitializeParams(
                    image=image,
                    disk_size_gb=disk_size,
                )
            ),
            network_interfaces=[compute.InstanceNetworkInterface(
                network="default"
            )],
        )

        # Exportar información de la VM
        self.instance_name = instance.name
        self.register_outputs({"instance_name": self.instance_name})
