import glob
import pybrain
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import matplotlib.pyplot as plt
import datetime
import random
import ast
import time
import sqlalchemy
from sqlalchemy import *
from sqlalchemy import event
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
import urllib2
import urllib
import json
import glob
import pprint
import dateutil.parser
import pprint
import re
from sklearn import linear_model, datasets
import time
from sklearn.naive_bayes import GaussianNB
import nltk
from collections import defaultdict
from sklearn import svm
pp = pprint.PrettyPrinter(indent=4)


import numpy
import time
import sqlalchemy
from sqlalchemy import *
from sqlalchemy import event
from sqlalchemy.dialects.mysql import LONGTEXT
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
import urllib2
import urllib
import json
import pprint
import dateutil.parser
import gevent
import datetime
import marshal

import re, math, collections, itertools
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
import numpy as np
import csv
import re
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from sklearn.svm import LinearSVC
from nltk.classify.scikitlearn import SklearnClassifier
import os

Base = declarative_base()
mysql_url = "mysql://forex:yummy4money@forex.c2ggnaqt6wye.us-west-1.rds.amazonaws.com/forex"
sqlite_url = 'sqlite:///database.db'
db = create_engine(mysql_url, echo=False)
session = sessionmaker()
session.configure(bind=db)
session = session()

class SensorUpdate(Base):
    __tablename__ = "sensor_updates"
    timestamp = Column(DateTime, primary_key = True)
    sensor_type = Column(String(40), primary_key = True)
    advertising_id = Column(String(40), primary_key = True) # probably 36 chars long
    value = Column(String(80))
    
    def __init__(self, advertising_id, timestamp, sensor_type, value):
        self.sensor_type = sensor_type
        self.advertising_id = advertising_id
        self.timestamp = timestamp
        self.value = value
Base.metadata.create_all(db)

	
from flask import Flask, request
app = Flask(__name__)

@app.route('/sensor_update', methods=['POST', 'GET'])
def sensor_update():
    error = None
    if request.method == 'POST':
        try:
            for key in request.form.keys():
                if "data" in key:
                    item = SensorUpdate(request.form['advertisingID'], datetime.datetime.now(), key, request.form[key])
                    session.add(item)
                    session.commit()
            print "Successfully Loaded Update from ID " + request.form['advertisingID']
            return "Update Received Successfully"
        except:
            print "Failed to handle update"
            return "Update Received With Error"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
        
    return "Do Not Accept HTTP GET requests"
	
#app.debug = True
app.run(host= '0.0.0.0')
