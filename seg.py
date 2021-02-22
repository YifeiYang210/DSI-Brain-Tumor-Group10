import argparse
import logging
import sys
import os
import shutil
import random
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from sklearn.metrics import accuracy_score

import tensorflow as tf
import tensorflow.keras.backend as K

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

from tensorflow.keras.preprocessing.image import ImageDataGenerator

data_root = r"C:\Users\63423\Documents\#work\DSI"

x = ImageDataGenerator()

def get_args():
    parser = argparse.ArgumentParser(description='Train the UNet',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-e', '--epochs', metavar='E', type=int, default=5,
                        help='Number of epochs', dest='epochs')
    parser.add_argument('-b', '--batch-size', metavar='B', type=int, nargs='?', default=1,
                        help='Batch size', dest='batchsize')
    parser.add_argument('-l', '--learning-rate', metavar='LR', type=float, nargs='?', default=0.0001,
                        help='Learning rate', dest='lr')
    parser.add_argument('-f', '--load', dest='load', type=str, default=False,
                        help='Load model from a .h5 file')   # pth -> h5
    # parser.add_argument('-s', '--scale', dest='scale', type=float, default=0.5,
    #                     help='Downscaling factor of the images')
    # parser.add_argument('-v', '--validation', dest='val', type=float, default=10.0,
    #                     help='Percent of the data that is used as validation (0-100)')

    return parser.parse_args()


if __name__ == '__main__':

    # 1. 导入环境，并初始化
    args = get_args()
    config = ConfigProto()
    config.gpu_options.allow_growth = True  # 设置gpu
    # use CPU to train your model, please add " os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

    session = InteractiveSession(config=config)

    log_path = os.path.join("./logs/", args.epochs, "_", args.model)
    logging.basicConfig(level=logging.INFO, filename=log_path, filemode='a', format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
    cpus = tf.config.experimental.list_physical_devices(device_type='CPU')
    logging.info(f'Using device {gpus} \n {cpus} \n')

    net = UNet_3Plus.UNet_3Plus_DeepSup()

    if args.load:
        net.load_state_dict(
            torch.load(args.load, map_location=device)
        )
        logging.info(f'Model loaded from {args.load}')

    net.to(device=device)

    session.close()
