import logging
import os
import smm
from smm.classifier.textprocessing import TwitterProcessor

basepath =  os.path.realpath(os.path.join(os.path.dirname(smm.__file__),'..'))

# MongoDB
mongo_db = dict(db='smm', host='localhost', port=27017, is_slave=False, read_preference=False,
                slaves=None, username=None, password=None)


#test db
test_mongo_db = dict(db='smm_test', host='localhost', port=27017, is_slave=False, read_preference=False,
                     slaves=None, username=None, password=None)


# Classifiers
# default training set
classifier="bayes"
# default tokenizer
classifier_tokenizer = TwitterProcessor
# number of classifier processes to start (should not exceed number of cpu cores)
classifier_pool_size = 1


# TWITTER
twitter_oauth_token = "56356461-zNcAX7r9hAWDIyFsM4c7RPGiWXWGy6scZHyMV2iFq"
twitter_oauth_secret = "IBjA1GduRzPvcdgHuYJRGeZ9TzYATnWhvk0vhIUZ5k"
twitter_oauth_custkey = "mgmZOhFNnv54MvmAEjaWbw"
twitter_oauth_custsecret = "u3fAm8u99ZGB10wjzWp77d1llp5ExCksbUhNjb0b8"

#sleep for x seconds if twitter raises httpError exception
twitter_http_error_sleep = 10

#how often should we check for changed keywords
twitter_kw_interval_check = 10


# Server Flask
server_host = '0.0.0.0'
server_port = 5000
server_templates = os.path.join(basepath, 'resources', 'templates')
server_static = os.path.join(basepath, 'resources', 'static')
server_debug = True
server_max_connection_per_ip = 2

server_socketio_handlers = ['websocket', 'xhr-polling', 'xhr-multipart', 'jsonp-polling']


# Logging
logfile_path = os.path.join(basepath, 'smm.log')
# default logging to console
logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(levelname)s %(message)s')

# log INFO to file as well
filelog = logging.FileHandler(logfile_path, 'w')
filelog.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
filelog.setFormatter(formatter)
logging.getLogger('').addHandler(filelog)

