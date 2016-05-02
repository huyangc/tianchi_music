# -*- coding: utf-8 -*-
# @Date    	: 2016-04-08 20:26:35
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com
# refer		:http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#example-linear-model-plot-ols-py
import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from matplotlib.legend_handler import HandlerLine2D

#--------stable-------------------
import os,sys
path = os.getcwd()
parent_path = os.path.dirname(path)
parent_path = os.path.dirname(parent_path)	#notice
sys.path.append(parent_path)
import static_data as sd
CURRENT_PATH=sd.CURRENT_PATH
ARTIST_FOLDER=sd.ARTIST_FOLDER
ARTIST=sd.ARTIST
SONGS=sd.SONGS
SONG_P_D_C=sd.SONG_P_D_C
ARTIST_P_D_C=sd.ARTIST_P_D_C
SONG_FAN=sd.SONG_FAN
ARTIST_FAN=sd.ARTIST_FAN
DAYS=sd.DAYS
START_UNIX  =sd.START_UNIX
DAY_SECOND  =sd.DAY_SECOND
START_WEEK=sd.START_WEEK
#--------stable-------------------

def num2Week(num):
	week=(START_WEEK+num)%7
	if week==0:
		return 7
	return week
'''
songs is a table:
row:DAYS=183
column:2(index,num2Week)+len(songs_list)+result(sum of play)
'''
def loadData(artist):
	songs=[[i,num2Week(i)] for i in range(DAYS)]
	songs_list={}
	index=0
	with open(ARTIST) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			if artist==row[1]:
				songs_list[row[0]]=index
				index+=1
				songs[0].append(int(row[3]))
	
	for i in range(1,DAYS):
		for j in range(index):
			songs[i].append(0)
	
	with open(SONG_P_D_C,'r',encoding='utf-8') as fr:
			songs_id=fr.readline().strip('\n')
			while songs_id:
				play=list(map(int,fr.readline().strip('\n').split(',')))
				download=list(map(int,fr.readline().strip('\n').split(',')))
				collect=list(map(int,fr.readline().strip('\n').split(',')))
				if songs_id in songs_list:
					for i in range(1,DAYS):
						songs[i][2+songs_list[songs_id]]=songs[i-1][2+songs_list[songs_id]]+play[i-1]
				songs_id=fr.readline().strip('\n')

	with open(ARTIST_P_D_C,'r',encoding='utf-8') as fr:
		artist_id=fr.readline().strip('\n')
		while artist_id:
			play=list(map(int,fr.readline().strip('\n').split(',')))
			download=list(map(int,fr.readline().strip('\n').split(',')))
			collect=list(map(int,fr.readline().strip('\n').split(',')))
			if artist==artist_id:
				for i in range(DAYS):
					songs[i].append(play[i])
			artist_id=fr.readline().strip('\n')
	return songs

diabetes=loadData('0c80008b0a28d356026f4b1097041689')
diabetes=np.array(diabetes)
diabetes_X=diabetes[:,1:-1]
diabetes_Y=diabetes[:,-1]
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_Y[:-30]
diabetes_y_test = diabetes_Y[-30:]

# Create linear regression object
#regr = linear_model.LinearRegression()
regr = linear_model.Ridge (alpha = .05,fit_intercept=False)
# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The intercept
print('Intercept: \n', regr.intercept_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
plt.scatter(diabetes[:,0][:-30], diabetes_y_train,  color='black')
plt.scatter(diabetes[:,0][-30:], diabetes_y_test,  color='red')
train=plt.plot(diabetes[:,0][:-30], regr.predict(diabetes_X_train), color='black',
         linewidth=3)
test=plt.plot(diabetes[:,0][-30:], regr.predict(diabetes_X_test), color='red',
         linewidth=3)
plt.legend([train[0], test[0]], ["train","test"])
plt.show()