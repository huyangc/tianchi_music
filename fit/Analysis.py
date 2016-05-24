import time
import numpy as np
import csv
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from matplotlib.legend_handler import HandlerLine2D
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

# --------stable-------------------
import os, sys

path = os.getcwd()
parent_path = os.path.dirname(path)
sys.path.append(parent_path)

import static_data as sd

CURRENT_PATH = sd.CURRENT_PATH
ARTIST_FOLDER = sd.ARTIST_FOLDER
USER_FOLDER = sd.USER_FOLDER
ARTIST = sd.ARTIST
SONGS = sd.SONGS
SONG_P_D_C = sd.SONG_P_D_C
ARTIST_P_D_C = sd.ARTIST_P_D_C
USER_P_D_C = sd.USER_P_D_C
SONG_FAN = sd.SONG_FAN
ARTIST_FAN = sd.ARTIST_FAN
DAYS = sd.DAYS
START_UNIX = sd.START_UNIX
DAY_SECOND = sd.DAY_SECOND
START_WEEK = sd.START_WEEK
ALL_USER = sd.ALL_USER
ALL_USER_INFO = sd.ALL_USER_INFO
USER_SONG_RELATION = sd.USER_SONG_RELATION
USER_SONG_FOLDER = sd.USER_SONG_FOLDER
ALL_SONG = sd.ALL_SONG
SONG_INFO = sd.SONG_INFO
USER_INFO_FILTER = sd.USER_INFO_FILTER
SONG_FEATURE = sd.SONG_FEATURES
SONG_UNIQUE_USER = sd.SONG_UNIQUE_USER
TRAINING_LABEL = sd.TRAINING_LABEL
GBR_RESULT = "GBR_result"
RECENT_DAYS_LIST = [1, 2, 3, 7, 14, 21, 28, 35, 42, 49, 56]

songInfo = pickle.load(open(SONG_INFO, 'rb'))
songFans = pickle.load(open(SONG_UNIQUE_USER, 'rb'))

def generateFeatures(doAnyway=False):
    if not doAnyway:
        if os.path.exists(SONG_FEATURE) and os.path.exists(TRAINING_LABEL):
            ret = pickle.load(open(SONG_FEATURE, 'rb'))
            trl = pickle.load(open(TRAINING_LABEL, 'rb'))
            return ret, trl
    song_features = {}

    training_label = {}
    for i in songInfo:
        features = []
        label = []
        print("%s len of day: %d" % (i, len(songInfo[i][0])))
        for dt in range(60, 120, 1):
            feature = []
            for day in RECENT_DAYS_LIST:
                feature.append(np.sum(songInfo[i][0][dt - day:dt]))
                feature.append(np.sum(songInfo[i][1][dt - day:dt]))
                feature.append(np.sum(songInfo[i][2][dt - day:dt]))
                feature.append(
                    0 if songFans.get(i) is None else np.sum([len(songFans[i][j]) for j in range(dt - day, dt)]))
                # print(songFans)
            label.append(songInfo[i][0][dt])
            features.append(feature)
        training_label[i] = label
        song_features[i] = features
    pickle.dump(song_features,open(SONG_FEATURE,'wb'))

    pickle.dump(training_label, open(TRAINING_LABEL, 'wb'))
    return song_features, training_label

def generateTestData(label_data,dt):
    feature = []
    for day in RECENT_DAYS_LIST:
        feature.append(np.sum(label_data[dt - day:dt]))
        feature.append(0)
        feature.append(0)
        feature.append(
            0 if songFans.get(i) is None else np.sum([len(songFans[i][j]) for j in range(dt - day, dt)]))
        # print(songFans)
    return feature


def trainModelUsingRFR(training_data, label_data,songid):  # RFR:RandomForestRegressor
    model = RandomForestRegressor(n_estimators=100)
    label = np.asarray(label_data).reshape(len(label_data),1)
    print (label.shape)
    model.fit(training_data,pd.DataFrame(label).values.ravel())
    for i in range(120,183,1):
        feature = generateTestData(label_data,i)
        ret = model.predict(np.asarray(feature).reshape(1,-1))
        print(i,ret[0],songInfo[songid][0][i])
        label_data.append(ret[0])



def trainModelUsingGBR(training_data,label_data,songid):
    fw = open(GBR_RESULT,'a')
    model = GradientBoostingRegressor()
    label = np.asarray(label_data).reshape(len(label_data), 1)
    print(label.shape)
    model.fit(training_data, pd.DataFrame(label).values.ravel())
    fw.write(songid+'\n')
    for i in range(120, 183, 1):
        feature = generateTestData(label_data, i)
        ret = model.predict(np.asarray(feature).reshape(1, -1))
        fw.write(str(i)+'\t'+str(ret[0])+'\t'+str(songInfo[songid][0][i])+'\n')
        label_data.append(ret[0])

if __name__ == "__main__":
    songFeature, training_label = generateFeatures()
    for i in songFeature:
        training_data = pd.DataFrame(np.asmatrix(songFeature[i]))
        if os.path.exists(i + ".csv"):
            training_data.to_csv(i + ".csv")
        trainModelUsingGBR(songFeature[i],training_label[i],i)