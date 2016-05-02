#阿里音乐流行趋势预测大赛，数据图像化模块

> 这个目录下应该有阿里云的2个文件，由于太大就没有上传  

###主要功能有以下几个:
* ifNoSongTXT() 将目标mars_tianchi_user_actions.csv进行数据整理，整理后得到2个文件:  
	- song_p_d_c.txt:  
		+ 第一行 songs_id  
		+ 第二行 每天的播放量  
		+ 第三行 每天的下载量  
		+ 第四行 每天的收藏量  
		+ PS:上面的数据都是直接使用的，没有考虑用户的重复操作  
	- song_fan.txt:  
		+ 第一行 songs_id  
		+ 第二行 每天的不同用户的数目  
		+ PS:这里只包括action=1的类型,具体为什么，请自己思考   

* ifNoArtistTXT() 对artist的songs进行整体整理，整理后得到2个文件:
	- artist_p_d_c.txt:   
		+ 第一行 artist_id  
		+ 第二行 每天的播放量  
		+ 第三行 每天的下载量  
		+ 第四行 每天的收藏量  
		+ PS:上面的数据都是直接使用的，没有考虑用户的重复操作  
	- artist_fan.txt:   
		+ 第一行 artist_id  
		+ 第二行 每天的不同用户的数目  
		+ PS:这里只包括action=1的类型,具体为什么，请自己思考   

* class artist() 处理单个艺人，方便对单个艺人进行分析:  
     	- __init__(self) 自动创建所需文件，需要自己建立artist目录   
     	- plot_artist_play(self) 绘制艺人的播放，下载，收藏的总图    
     	- plot_artist_fan(self) 绘制艺人每天的不同用户的数量  
     	- plot_song_play(self) 绘制当前艺人每首歌曲的播放，下载，收藏的图片  
     	- plot_song_fan(self) 绘制当前歌曲每天的不同用户的数量  

### 建议函数使用顺序:
```python
ifNoSongTXT()
ifNoArtistTXT()#PS:这里必须要先执行

#下面的方法可以随意调用
a=artist('0c80008b0a28d356026f4b1097041689')
a.plot_artist_play()
a.plot_artist_fan()
a.plot_song_play()
a.plot_song_fan()
```
