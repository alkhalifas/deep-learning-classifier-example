# -*- coding: utf-8 -*-
"""Classifier model"""

# internal
from .base_model import BaseModel
from dataloader.dataloader import DataLoader

# external
import tensorflow as tf


class Classifier(BaseModel):
    """Unet Model Class"""
    def __init__(self, cfg):
        pass

    def load_data(self):
        pass

    def build(self):
        pass

    def train(self):
        pass

    def evaluate(self):
        pass