import os
import logging
import utils.configvariables as uc
from utils.s3_manager import load_to_s3, get_file
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


class Predict:

    def feature_engineering(self):
        """
        Prepare the data for the model
        :return:
        """
        log.info('feature_engineering: Start...')
        data_prepare = DataPrepare()
        data_prepare.do_something()
        return

    def predict_get_pickle(self):
        """
        Get the train model from a bucket
        :return: file object
        """
        log.info('predict_get_pickle: Start...')
        train_file_name = 'model.pkl'
        remote_s3_filename = os.path.join(uc.env_folder_model, train_file_name)
        return get_file(uc.env_bucket_model, remote_s3_filename)

    def predict_process(self):
        """
        Predict the train model
        :return:
        """
        log.info('predict_process: Start...')
        return

    def predict_model(self):
        self.predict_get_pickle()
        self.feature_engineering()
        self.predict_process()
