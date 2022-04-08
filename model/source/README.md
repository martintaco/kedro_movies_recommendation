# Analytical Model Pipeline

# Table of Contents

- [Analytical Model Pipeline](#analytical-model-pipeline)
- [Table of Contents](#table-of-contents)
  - [1. Analitical Conceptual Chart](#1-analitical-conceptual-chart)
   

## 1. Analitical Conceptual Chart
*Put the flow diagram for the execution by showing all the steps that we have for training and predict*


Docker commands:
```
docker build -t [ContainerName] .

docker run -e BUCKET_MODEL='xxxx' -e FOLDER_MODEL='xxx-xxx' -e CODPAIS='xx' -e RS_HOST='xx.xx.xx.xx' -e RS_PORT='5439' -e RS_DATABASE='analitico' -e RS_USER='xxxx' -e RS_PASSWORD='xxxx' -e ENV_DEPLOY='prd' -e AWS_ACCESS_KEY_ID='xxxx' -e AWS_SECRET_ACCESS_KEY='xxxx' -e AWS_DEFAULT_REGION='us-east-1' -ti [ContainerName] python run_step.py [params]


```


Other Docker Commands:
```
docker images

docker ps

docker exec -it <container_id> /bin/bash

docker rmi -f <container_name>

docker ps -aq --no-trunc -f status=exited | xargs docker rm
```
