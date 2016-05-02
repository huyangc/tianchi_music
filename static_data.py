# -*- coding: utf-8 -*-
# @Date    	: 2016-04-21 20:57:54
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

import sys,os


CURRENT_PATH=sys.path[-1]
ARTIST_FOLDER=os.path.join(CURRENT_PATH,'pic','artist')

ARTIST=os.path.join(CURRENT_PATH,'mars_tianchi_songs.csv')
SONGS=os.path.join(CURRENT_PATH,'mars_tianchi_user_actions.csv')

SONG_P_D_C=os.path.join(CURRENT_PATH,'song_p_d_c.txt')
ARTIST_P_D_C=os.path.join(CURRENT_PATH,'artist_p_d_c.txt')

SONG_FAN=os.path.join(CURRENT_PATH,'song_fan.txt')
ARTIST_FAN=os.path.join(CURRENT_PATH,'artist_fan.txt')

DAYS=183		#HOW MANY DAYS YOU WANT TO RECORD.

START_UNIX 	=1425139200
DAY_SECOND 	=86400

START_WEEK=7
