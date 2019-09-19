import os, logging, sys
from datetime import date

def init_log():
    log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep), 'logs')
    log_fname =  'logfile_' + str(date.today())
    logging.basicConfig(
        format='%(asctime)s %(levelname)8s %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler("{0}/{1}.log".format(log_dir, log_fname)),
            logging.StreamHandler()
        ]
    )
