# -*- coding: utf-8 -*-
# @Date    	: 2016-04-21 20:57:54
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

import sys,os


CURRENT_PATH=sys.path[-1]
ARTIST_FOLDER=os.path.join(CURRENT_PATH,'pic','artist')
USER_FOLDER=os.path.join(CURRENT_PATH,'pic','user')

ARTIST=os.path.join(CURRENT_PATH,'../data/mars_tianchi_songs.csv')
SONGS=os.path.join(CURRENT_PATH,'../data/mars_tianchi_user_actions.csv')

SONG_P_D_C=os.path.join(CURRENT_PATH,'song_p_d_c.txt')
ARTIST_P_D_C=os.path.join(CURRENT_PATH,'artist_p_d_c.txt')
USER_P_D_C=os.path.join(CURRENT_PATH,"user_p_d_c.txt")

SONG_FAN=os.path.join(CURRENT_PATH,'song_fan.txt')
ARTIST_FAN=os.path.join(CURRENT_PATH,'artist_fan.txt')

DAYS=183		#HOW MANY DAYS YOU WANT TO RECORD.

START_UNIX 	=1425139200
DAY_SECOND 	=86400

START_WEEK=7

ALL_USER=os.path.join(CURRENT_PATH,"user.dat")
ALL_USER_INFO=os.path.join(CURRENT_PATH,"userinfo.dat")
USER_SONG_RELATION=os.path.join(CURRENT_PATH,"user_song.dat")
USER_SONG_FOLDER = os.path.join(CURRENT_PATH,"user_song")
ALL_SONG = os.path.join(CURRENT_PATH,"all_song.dat")
SONG_INFO = os.path.join(CURRENT_PATH,"song_info.dat")
USER_INFO_FILTER = os.path.join(CURRENT_PATH,"userinfo_filtered.dat")
SONG_FEATURES = os.path.join(CURRENT_PATH,"song_feature.dat")
SONG_UNIQUE_USER = os.path.join(CURRENT_PATH,"song_unique_user.dat")
TRAINING_LABEL= os.path.join(CURRENT_PATH,"training_label.dat")