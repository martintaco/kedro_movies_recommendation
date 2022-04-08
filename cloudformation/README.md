# CloudFormation Templates
In this folder we will find all the services that the aplication ***Aplication-Name*** will need to be deployed.

*In this doc, please describe each CloudFormation template, describe them consider the current folder structure.*

# Table of Contents

* [1 Deploy](#1-Deploy)
  * [1.2 < Template File >](#12--template-file-)
* [2 Setup](#2-Setup)
  * [2.2 < Template File >](#22--template-file-)

## 1. Deploy

***- Deploy (services that can be deployed more that once)***

### 1.2 cloudformation_[project_name]_deploy

+ Template only is a reference
+ What this template does? Create some services.

| Services        | Services Name                  | Enviroments   |
|-----------------|--------------------------------|---------------|
| ECS             | ecs-{projectname}-model-{env}          | prd, qas, dev |
| Task Definition | td-bigdata-{projectname}-{env}         | prd, qas, dev |
| SNS             | SNS-Datalake-Model-{projectname}-{env} | prd, qas, dev |

+ Parameters that this template will use:*

| Paramaters           | Values                         | Examples                                   |
|----------------------|--------------------------------|--------------------------------------------|
| AppEnv               | prd, qas, dev                  | dev                                        |
| Env                  | PRD, QAS, DEV                  | DEV                                        |
| FolderModel          | <Folder name in Bucket models> | template                                   |
| ProjectName          | <Project Name>                 | template                                   |
| PrincipalProjectName | <Princial Project>             | bigdata                                    |
| RedshiftDBPassword   | XXXX                           | Belcorp2345                                |
| RedshiftDBUser       | XXXX                           | usr_app_template                           |
| RedshiftDatabaseName | analitico                      | analitico                                  |
| RedshiftHost         | XXXX                           | 10.12.14.16                                |
| RedshiftEnvPort      | 5439                           | 5439                                       |
| MLFlowHost           | mlflow.url.com                 | alb-template.elb.amazonaws.com             |

+ All these services are used for the MLOps case.

## 2. Setup

***- Setup (services that has to be deployed once)***

*Consider that the setup services need a CloudFormation template and all the detail of the service,because that services will be request for deploying by Jira*
*The services in the setup folder are DynamoDb, IAM Roles, Security Groups,SNS,SQS.*

### 2.2 cloudformation_[project_name]_setup

+ Template only is a reference
+ What this template does? Create some services.

| Services | Services Name                        | Enviroments   |
|----------|--------------------------------------|---------------|
| Role     | bigdata_{projectname}_{env}         | prd, qas, dev |
| Policy   | policy_bigdata_{projectname}_{env}  | prd, qas, dev |
| LogGroup | /ecs/forecast/td-bigdata-fania-{env} | prd, qas, dev |
| ECR      | bigdata/{project_name}-model         |               |

+ Parameters that this template will use:*

| Paramaters  | Values        | Examples |
|-------------|---------------|----------|
| AppEnv      | qas           | qas      |
| Env         | QAS           | QAS      |
| ProjectName | <ProjectName> | template |

+ All these services are used for the MLOps case.

