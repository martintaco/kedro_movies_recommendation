import os
import shutil
import gzip

env_bucket_model = os.environ.get('BUCKET_MODEL', '')
env_folder_model = os.environ.get('FOLDER_MODEL', '')
env_rs_host = os.environ.get('RS_HOST', '')
env_rs_port = os.environ.get('RS_PORT', '')
env_rs_database = os.environ.get('RS_DATABASE', '')
env_rs_user = os.environ.get('RS_USER', '')
env_rs_password = os.environ.get('RS_PASSWORD', '')
env_deploy = os.environ.get('ENV_DEPLOY', '')

env_redshift_role = os.environ.get('REDSHIFT_ROLE')
env_orchestrator_arn = os.environ.get('ARN_ORCHESTRATOR')
env_ml_flow_host = os.environ.get('MLFLOW_HOST')
env_ml_flow_project = env_folder_model


script_prepare = 'data_prepare/scripts/script_prepare.sql'

product_feature = 'product-features'
user_products = 'user-products'
user_features = 'user-features'

# origin folder
local_folder = os.path.dirname(os.path.abspath(__file__))
# LOG Files
LOG_FILE_APP = 'log_app.log'
LOCAL_LOG_DIR = os.path.join(local_folder, 'Log')
FILE_APP = FILE_APP = os.path.join(LOCAL_LOG_DIR, LOG_FILE_APP)


def zip_file(file_name_in, file_name_out=""):
    file_name_out = file_name_out if file_name_out != "" else file_name_in+".gz"
    with open(file_name_in, 'rb') as f_in:
        with gzip.open(file_name_out, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return file_name_out
