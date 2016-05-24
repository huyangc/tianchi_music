# -*- coding: utf-8 -*-
# @Date    	: 2016-04-08 22:25:20
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com
# refer		: http://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html#example-linear-model-plot-ridge-path-py

import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

import os,sys
path = os.getcwd()
parent_path = os.path.dirname(os.path.dirname(path))
sys.path.append(parent_path)

import static_data as sd
CURRENT_PATH=sd.CURRENT_PATH
ARTIST_FOLDER=sd.ARTIST_FOLDER
USER_FOLDER=sd.USER_FOLDER
ARTIST=sd.ARTIST
SONGS=sd.SONGS
SONG_P_D_C=sd.SONG_P_D_C
ARTIST_P_D_C=sd.ARTIST_P_D_C
USER_P_D_C=sd.USER_P_D_C
SONG_FAN=sd.SONG_FAN
ARTIST_FAN=sd.ARTIST_FAN
DAYS=sd.DAYS
START_UNIX  =sd.START_UNIX
DAY_SECOND  =sd.DAY_SECOND
START_WEEK=sd.START_WEEK

"""
{songs_id:bool,songs_id:bool,...,songs_id:bool}
"""
def getSongsListByArtist_id(artist):
    songs = {}
    with open(ARTIST) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        for row in spamreader:
            if artist==row[1]:
                songs[row[0]] = True
    return songs
'''
return:
	[]:size for 183
'''
def loadData(artist):
	songs=getSongsListByArtist_id(artist)
	with open(ARTIST_P_D_C,'r',encoding='utf-8') as fr:
		artist_id=fr.readline().strip('\n')
		while artist_id:
			play=list(map(int,fr.readline().strip('\n').split(',')))
			download=list(map(int,fr.readline().strip('\n').split(',')))
			collect=list(map(int,fr.readline().strip('\n').split(',')))
			if artist==artist_id:
				return play
			artist_id=fr.readline().strip('\n')

X=[i for i in range(183)]
X=np.array(X)
X=X[:, np.newaxis]
diabetes_Y=loadData('40bbb0da5570702dd6ff3af5e9e3aea6')

y = np.ones(10)

###############################################################################
# Compute paths

n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)
clf = linear_model.Ridge(fit_intercept=False)

coefs = []
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)

###############################################################################
# Display results

ax = plt.gca()
ax.set_color_cycle(['b', 'r', 'g', 'c', 'k', 'y', 'm'])

ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim()[::-1])  # reverse axis
plt.xlabel('alpha')
plt.ylabel('weights')
plt.title('Ridge coefficients as a function of the regularization')
plt.axis('tight')
plt.show()

