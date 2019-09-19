import os, logging
from datetime import date

def init_log():
    log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep), 'logs')
    log_fname = os.path.join(log_dir, 'logfile_' + str(date.today()) + '.log')
    logging.basicConfig(
        format='%(asctime)s %(levelname)8s %(message)s',
        filename=log_fname, filemode='w', level=logging.DEBUG)
