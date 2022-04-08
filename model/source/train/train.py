import os
import logging
import utils.configvariables as uc
from utils.s3_manager import load_to_s3
from data_prepare.dataprepare import DataPrepare
import numpy as np
import pandas as pd

import pickle


# Setup logging
log = logging.getLogger(__name__)
log.setLevel(level=logging.INFO)
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler(uc.FILE_APP, mode='w')
log.addHandler(fh)


class Train:

    def feature_engineering(self):
        """
        Prepare the data for the model
        :return:
        """
        log.info('feature_engineering: Start...')
        data_prepare = DataPrepare()
        data_prepare.do_something()
        return

    def train_process(self):
        """
        Process the train model
        :return:
        """
        log.info('train_process: Start...')
        return

    def train_eval(self):
        """
        Evaluate the train model, optional
        :return:
        """
        log.info('train_eval: Start...')
        return

    def train_load(self, model_instance):
        """
        Serialize and Load the train model to a bucket
        :param model_instance: model instance
        :return: boolean
        """
        log.info('train_load: Start...')
        train_file_name = 'model.pkl'
        local_file_name = os.path.join(uc.local_folder, train_file_name)
        remote_s3_filename = os.path.join(uc.env_folder_model, train_file_name)

        model_serialize = open(local_file_name , 'wb')
        pickle.dump(model_instance, model_serialize)
        model_serialize.close()

        load_to_s3(uc.env_bucket_model, remote_s3_filename, local_file_name)
        return

    def train_model(self):
        """
        ####  PRINCIPAL TRAIN ###
        :return:
        """
        log.info('train_model: Start...')
        # self.feature_engineering()
        # self.train_process()
        # self.train_eval()
        # self.train_load()
        return

