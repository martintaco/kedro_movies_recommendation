import sys
import pickle


def validate_model(models, params):
    data = models(params)
    return data


def validate_data(x,y):
    data = x*y*2
    return data


def test_connection():
    assert validate_data(2,3) == 12


def test_model():
    models = None
    assert validate_model(models, [2,3]) == 3.2
