import os, logging, sys
from datetime import date


def init_log():
    log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep), 'logs')
    log_fname =  'logfile_' + str(date.today())
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
        # stream=sys.stdout,
        handlers=[
            logging.FileHandler("{0}/{1}.log".format(log_dir, log_fname)),
            # logging.StreamHandler(sys.stdout)
        ]
    )

    # logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))