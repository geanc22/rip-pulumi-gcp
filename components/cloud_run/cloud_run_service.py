import pulumi
import pulumi_gcp as gcp
import json

class CloudRunService(pulumi.ComponentResource):
    def __init__(self, name: str, image: str, opts: pulumi.ResourceOptions = None):
        super().__init__("custom:resource:CloudRunService", name, {}, opts)

        # Habilitar Cloud Run API
        # # service_api = gcp.projects.Service(
        # #     f"{name}-api",
        # #     service="run.googleapis.com",
        # #     disable_dependent_services=True
        # # )

        # Crear el servicio de Cloud Run
        service = gcp.cloudrun.Service(
            name,
            location="southamerica-west1",
            template={
                "spec": {
                    "containers": [{
                        "image": image,
                        "ports": [{"container_port": 8080}]
                    }]
                }
            },
            #opts=pulumi.ResourceOptions(depends_on=[service_api])
        )

        # Hacer el servicio accesible públicamente (opcional)
        #para verlo si hay politica organizacional -->
    #     curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
    # https://my-cloud-run-service-5ebbe04-7jdf3kckyq-tl.a.run.app/

       
        # # iam_policy = gcp.cloudrun.IamPolicy(
        # #     f"{name}-iam",
        # #     location=service.location,
        # #     project=service.project,
        # #     service=service.name,
        # #     policy_data = pulumi.Output.all(service.id).apply(lambda service_id: json.dumps({
        # #         "bindings": [
        # #             {
        # #                 "role": "roles/run.invoker",
        # #                 "members": ["user:rip@analitikacloud.com"]  # Cambia esto por el usuario que usará el servicio
        # #             }
        # #         ]
        # #     }))
            #ver politica de cloud run -->
             #gcloud run services get-iam-policy my-cloud-run-service-5eba735 --region=southamerica-west1 --project=rip-gti-desa


            # policy_data=pulumi.Output.all(service.id).apply(lambda service_id: f"""
            # bindings:
            # - role: roles/run.invoker
            #   members:
            #   - allUsers
            # """)
            
        ##)

        # Exportar la URL del servicio
        self.url = service.statuses.apply(lambda statuses: statuses[0]["url"] if statuses else None)

        self.register_outputs({"url": self.url})
