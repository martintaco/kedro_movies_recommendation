# CloudFormation Templates
En este folder se encuentran los templates a utilizar para el despliegue de colorimetro

### 1. training_setup

Este template despliega los siguientes servicios: 
- **IAM Role**: Permisos sobre el task Definition
- **AWS ECR**: Container donde se almacenara las versiones de imagen del training

Que son los servicios que se utilizaran dentro del template de deploy. 

Considerar que el setup en un nivel de QAS y PRD se despliega en la cuenta belcorp, y por politica se crean estos servicios mediante Jira, se deberian crear los nombres de los servicios de acuerdo a como estan en el template. 

### 2. training_deploy

Este template desplegara los servicios que necesitara colorimetro para poder integrarse con la solucion de MLOPS, considerarse que los nombres definidos para los servicios son los que utilizaria la solucion de MLOPS a fin de gatillar las ejecuciones

Los servicios que se despliegan: 
- **AWS SNS**: Topic por donde se enviara las notificaciones
- **AWS ECS**: Cluster donde se ejecutaran los containers
- **Task Definition**: Definicion de la tarea que se ejecutara, Recursos, variables de entorno e imagen que se utilizara. 
