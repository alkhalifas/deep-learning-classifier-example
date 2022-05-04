# -*- coding: utf-8 -*-
""" main.py """

from configs.config import CFG
from model.classifier import Classifier


def run():
    """Builds model, loads data, trains and evaluates"""
    model = Classifier(CFG)
    model.load_data()
    model.build()
    model.train()
    model.evaluate()


if __name__ == '__main__':
    run()