import mlflow
import uuid
import os


class MLFlowTracking:

    FOLDER_DATA = 'data'

    def __init__(self, ml_flow_host, ml_flow_port="5000"):
        self.ml_flow_uri = "http://{}:{}".format(ml_flow_host, ml_flow_port)
        mlflow.set_tracking_uri(self.ml_flow_uri)
        mlflow.tracking.MlflowClient(self.ml_flow_uri)
        self.active_run = None

    @staticmethod
    def get_experiment_id(ml_flow_project):
        m_dict = mlflow.get_experiment_by_name(ml_flow_project).__dict__
        return m_dict['_experiment_id']

    @staticmethod
    def generate_hashcode():
        return uuid.uuid4().hex

    def start_experiment(self, ml_flow_project, run_name="", folder_model=""):
        mlflow.set_experiment(ml_flow_project)
        experiment_id = self.get_experiment_id(ml_flow_project)

        run_name = run_name if run_name != "" else self.generate_hashcode()

        self.active_run = mlflow.start_run(
            experiment_id=experiment_id,
            run_name=run_name
        )
        return self.active_run

    def get_run_id(self):
        return self.active_run.info.run_id

    @staticmethod
    def model_logging_tags(dict_tags):
        for key in dict_tags.keys():
            mlflow.set_tag(key, dict_tags[key])

    @staticmethod
    def model_logging_params(dict_params):
        for key in dict_params.keys():
            mlflow.log_param(key, dict_params[key])

    @staticmethod
    def model_logging_metrics(dict_metrics):
        for key in dict_metrics.keys():
            mlflow.log_metric(key, dict_metrics[key])

    @staticmethod
    def model_logging_artifact(file_name, artifact_sub_folder):
        mlflow.log_artifact(file_name, artifact_path=artifact_sub_folder)

    def download_artifacts(self, artifacts_folder, local_directory):
        client = mlflow.tracking.MlflowClient()
        if not os.path.exists(local_directory):
            os.mkdir(local_directory)
        client.download_artifacts(self.get_run_id(), artifacts_folder, local_directory)

    def get_artifact_data_folder(self):
        return os.path.join(mlflow.get_artifact_uri(), self.FOLDER_DATA)

    def end_experiment(self):
        mlflow.end_run()

    def get_ml(self):
        return mlflow