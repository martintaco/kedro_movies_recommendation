import sys
import time
from data_prepare.dataprepare import DataPrepare
from train.train import Train
from predict.predict import Predict


def data_prepare(argv):
    """
    Invoke Data Prepare class to process data
    :param argv: arguments of call
    :return:
    """
    data = DataPrepare()
    data.do_something()
    return


def train_model(argv):
    """
    Invoke Train class to process data
    :param argv: arguments of call
    :return:
    """
    train = Train()
    train.train_model()
    return


def predict_model(argv):
    """
    Invoke Predict class to process data
    :param argv: arguments of call
    :return:
    """
    predict = Predict()
    predict.predict_model()
    return


def validate(argv):
    """
    Validate the model
    :param argv:
    :return:
    """
    pass


def test(argv):
    """
    Some function to evaluate
    :param argv:
    :return:
    """
    pass


if __name__ == "__main__":

    print('Start: ', time.strftime("%I:%M:%S %p", time.localtime()))

    if len(sys.argv) > 1:
        if sys.argv[1] == 'prepare':
            data_prepare(sys.argv)

        if sys.argv[1] == 'train':
            train_model(sys.argv)

        if sys.argv[1] == 'predict':
            predict_model(sys.argv)

        if sys.argv[1] == 'validate':
            validate(sys.argv)

        if sys.argv[1] == 'test':
            test(sys.argv)

    print('Finish: ', time.strftime("%I:%M:%S %p", time.localtime()))

