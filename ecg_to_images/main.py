import argparse
import configparser
import os
import time
from datetime import date

import logging
from .image_types.a_2d import EcgImagesA_2D
import sys

from .config_parser import read_config_file
from enum import Enum

def main():

    print("entry")
    start = time.perf_counter()
    init_log()
    ns = parse_cmd_arguments()

    # pass the namespace containing the args to read the config file
    # options = read_config_file(ns)
    config = configparser.ConfigParser()
    config.read('/home/george/Dropbox/personal/thesis/repos/ecg-images/ecg_to_images/config.ini')

    image_type = config.get('image','type')

    mod = sys.modules['ecg_to_images.image_types.a_2d']
    # call the method of the module dynamically using reflection to avoid typing 6 ifs
    clsname = getattr(mod, 'EcgImages' + image_type)

    runtime_cls = globals()['EcgImages' + image_type]
    getattr(clsname, 'create_images')(runtime_cls, config)

    image_obj = runtime_cls(10, 'NORMAL')

    print(image_obj)
    print(image_type.lower())
    image_obj.create_images(config)
    function_name = str(image_obj.create_images)


    # getattr(image_type.lower(), 'create_images')(config)
    # else:
    #     logging.ERROR("The dictionary is empty")

    end = time.perf_counter()
    elapsed = end - start
    print('The conversion took: {} seconds'.format(elapsed))


def init_log():
    log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep), 'logs')
    log_fname = os.path.join(log_dir, 'logfile_' + str(date.today())+ '.log')
    logging.basicConfig(
        format='%(asctime)s %(levelname)8s %(message)s',
        filename=log_fname, filemode='w', level=logging.DEBUG)


def parse_cmd_arguments():
    ap = argparse.ArgumentParser(description='Ecg-to-image converter tool')
    # use the default configuration files that it is inside the package
    ap.add_argument('-c',
                    '--config',
                    dest='config',
                    nargs='?',
                    required=True,
                    help='You have to specify the full absolute path to the configuration file')
    return ap.parse_args()