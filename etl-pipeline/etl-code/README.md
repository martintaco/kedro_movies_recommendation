# Aca van Python o Scala 
# SQL Files / Stored Procedures que se usan en el etl

# DIRECTORIO  bigdata-project-template/

```
python3 run_step.py local

export BUCKET_NAME=<MY_BUCKET>
export AWS_ACCESS_KEY_ID=<MY_KEY>
export AWS_SECRET_ACCESS_KEY=<MY_SECRET>

docker build -t test -f etl-pipeline/etl-code/Dockerfile .

docker run -e BUCKET_NAME='<MY_BUCKET>' -e AWS_ACCESS_KEY_ID='<MY_KEY>' -e  AWS_SECRET_ACCESS_KEY='<MY_SECRET>' -it test python3 run_step.py miprueba

```

