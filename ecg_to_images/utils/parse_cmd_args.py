import argparse

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
