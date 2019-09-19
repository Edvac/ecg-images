import time
import sys
import importlib

from ecg_to_images.image_types import a_2d, a_1d, b_1d, b_2d, c_2d, c_1d
from ecg_to_images.utils.create_logs import init_log
from ecg_to_images.utils.parse_cmd_args import  parse_cmd_arguments
from ecg_to_images.utils.parse_conf_file import parse_config_file


def main():

    print("entry")
    start = time.perf_counter()
    init_log()
    ns = parse_cmd_arguments()
    # pass the namespace containing the args to read the config file
    config_file = parse_config_file(ns)
    image_type = config_file.get('image', 'type')

    # call the method of the module dynamically using reflection to avoid typing 6 ifs

    mod = sys.modules['ecg_to_images.image_types.' + image_type.lower()]

    runtime_cls = getattr(mod, 'EcgImages' + image_type)
    getattr(runtime_cls, 'create_images')(runtime_cls, config_file)

    end = time.perf_counter()
    elapsed = end - start
    print('The conversion took: {} seconds'.format(elapsed))