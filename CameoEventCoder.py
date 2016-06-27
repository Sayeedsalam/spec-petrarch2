
import PETRreader
import PETRglobals
import petrarch2
import utilities

import logging
import time


class CameoEventCoder:
    
    def __init__(self, config_folder='data/config/', config_file='PETR_config.ini'):
        #cli_args = petrarch2.parse_cli_args()
        utilities.init_logger('PETRARCH.log')
        logger = logging.getLogger('petr_log')
        PETRglobals.RunTimeString = time.asctime()
        logger.info('Using Config file: ',config_file)
        PETRreader.parse_Config(utilities._get_data(config_folder, config_file))
        petrarch2.read_dictionaries()
    
    
    def encode(self, article):
        return petrarch2.gen_cameo_event(article)
     