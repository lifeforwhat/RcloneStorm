# RcloneStorm

# INTRO
![intro](https://user-images.githubusercontent.com/59600370/77850666-08723600-720f-11ea-9f52-3b33f31d27d7.jpg)

멀티프로세싱을 이용해 NIC 별로 트래픽을 분산해 최대한 빠르게 특정 팀 드라이브로 특정 폴더 내에 있든 모든 파일들을 쑤셔박는 PYTHON 스크립트

# SPEED
경기도 북부 지역 KT 8회선 기준
385.59 Mbps

403.35 Mbps

375.43 Mbps

361.84 Mbps

391.52 Mbps

394.76 Mbps

378.95 Mbps



# LOG
프로세스당 할당량 [10127, 10127, 10127, 10127, 10127, 10127, 10127, 10133]
UPLOAD START	 g01 	 torrents\-####- ###\#### # ### ###- - ##### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\#### # ### ###- - ##### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.###.##.###
UPLOAD START	 g01 	 torrents\###\### ###.###

COMMAND	 rclone move local:"torrents\###\### ###.###" g01:"TV\TEMP\###" --bind ###.###.###.#
UPLOAD START	 g01 	 torrents\##### ### ##\##### ##### ###.###

COMMAND	 rclone move local:"torrents\##### ### ##\##### ##### ###.###" g01:"TV\TEMP\##### ### ##" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD START	 g01 	 torrents\###!!\post#r.jpg

COMMAND	 rclone move local:"torrents\###!!\post#r.jpg" g01:"TV\TEMP\###!!" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\##### ### ##\##### ##### ###.###

UPLOAD START	 g01 	 torrents\##### ### ##\##### ### ## ###.###

COMMAND	 rclone move local:"torrents\##### ### ##\##### ### ## ###.###" g01:"TV\TEMP\##### ### ##" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\####\#

COMMAND	 rclone move local:"torrents\####\#" g01:"TV\TEMP\####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###!!\post#r.jpg

UPLOAD START	 g01 	 torrents\###!!\###.###

COMMAND	 rclone move local:"torrents\###!!\###.###" g01:"TV\TEMP\###!!" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\#

UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\###!!\###.###

UPLOAD START	 g01 	 torrents\###!!\##.###

COMMAND	 rclone move local:"torrents\###!!\##.###" g01:"TV\TEMP\###!!" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\###!!\##.###

UPLOAD START	 g01 	 torrents\###!!\##.###

COMMAND	 rclone move local:"torrents\###!!\##.###" g01:"TV\TEMP\###!!" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD DONE		 g01 	 torrents\###!!\##.###

UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\###!!\##.###

COMMAND	 rclone move local:"torrents\###!!\##.###" g01:"TV\TEMP\###!!" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD DONE		 g01 UPLOAD DONE			  g01torrents\###!!\##.### 	 torrents\####\###.###



UPLOAD START	 g01 	 torrents\####\fanart.jpg

COMMAND	 rclone move local:"torrents\####\fanart.jpg" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\###!!\#

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\###!!\#" g01:"TV\TEMP\###!!" --bind ###.###.#.#
COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD DONE		 g01 	 torrents\####\fanart.jpg

UPLOAD DONE		 g01 	 torrents\###!!\#

UPLOAD START	 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\post#r.jpg

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.##
COMMAND	 rclone move local:"torrents\####\post#r.jpg" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\###!!\crawl_info.txt

COMMAND	 rclone move local:"torrents\###!!\crawl_info.txt" g01:"TV\TEMP\###!!" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\post#r.jpg

UPLOAD DONE		 g01 	 torrents\###!!\crawl_info.txt

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\crawl_info.txt

COMMAND	 rclone move local:"torrents\####\crawl_info.txt" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\crawl_info.txt

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\#####.###

COMMAND	 rclone move local:"torrents\####\#####.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\#####.###

UPLOAD START	 g01 	 torrents\####\#####.###

COMMAND	 rclone move local:"torrents\####\#####.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\#####.###

UPLOAD START	 g01 	 torrents\### ###\#####.###

COMMAND	 rclone move local:"torrents\### ###\#####.###" g01:"TV\TEMP\### ###" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\##### ### ##\##### ### ## ###.###

UPLOAD START	 g01 	 torrents\##### ### ##\##### ### ## ###.###

COMMAND	 rclone move local:"torrents\##### ### ##\##### ### ## ###.###" g01:"TV\TEMP\##### ### ##" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\-####- ###\#### # ### ###- - ##### ##.###

UPLOAD START	 g01 	 torrents\-####- ###\#### 힙# ### - #### ### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\#### 힙# ### - #### ### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\##### ### ##\##### ### ## ###.###

UPLOAD START	 g01 	 torrents\##### ### ##\##### ### ## ###.###

COMMAND	 rclone move local:"torrents\##### ### ##\##### ### ## ###.###" g01:"TV\TEMP\##### ### ##" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\-####- ###\#### 힙# ### - #### ### ##.###

UPLOAD START	 g01 	 torrents\-####- ###\### TV ##### -## # ####- - #### ##### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\### TV ##### -## # ####- - #### ##### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\##.###

COMMAND	 rclone move local:"torrents\####\##.###" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\####\##.###

UPLOAD START	 g01 	 torrents\####\#

COMMAND	 rclone move local:"torrents\####\#" g01:"TV\TEMP\####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD DONE		 g01 	 torrents\####\#

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\####\###.###

COMMAND	 rclone move local:"torrents\####\###.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD DONE		 g01 	 torrents\####\###.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\South of H#ll\fanart.jpg

COMMAND	 rclone move local:"torrents\South of H#ll\fanart.jpg" g01:"TV\TEMP\South of H#ll" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\South of H#ll\fanart.jpg

UPLOAD START	 g01 	 torrents\South of H#ll\post#r.jpg

COMMAND	 rclone move local:"torrents\South of H#ll\post#r.jpg" g01:"TV\TEMP\South of H#ll" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\South of H#ll\post#r.jpg

UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\South of H#ll\##.###" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD DONE		 g01 	 torrents\##### ### ##\##### ### ## ###.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\##### ### ##\##### ### ## ###.###

UPLOAD DONE		 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\##### ### ##\##### ### ## ###.###" g01:"TV\TEMP\##### ### ##" --bind ###.##.###.###
UPLOAD START	 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\South of H#ll\##.###" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\South of H#ll\##.###

UPLOAD START	 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\South of H#ll\##.###" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\South of H#ll\##.###

UPLOAD START	 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\South of H#ll\##.###" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\South of H#ll\##.###

UPLOAD START	 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\South of H#ll\##.###" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\South of H#ll\##.###

UPLOAD START	 g01 	 torrents\South of H#ll\crawl_info.txt

COMMAND	 rclone move local:"torrents\South of H#ll\crawl_info.txt" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\South of H#ll\crawl_info.txt

UPLOAD START	 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\South of H#ll\##.###" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\South of H#ll\##.###

UPLOAD START	 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\South of H#ll\##.###" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\South of H#ll\##.###

UPLOAD START	 g01 	 torrents\South of H#ll\##.###

COMMAND	 rclone move local:"torrents\South of H#ll\##.###" g01:"TV\TEMP\South of H#ll" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\crawl_info.txt

COMMAND	 rclone move local:"torrents\### ### ####\crawl_info.txt" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\South of H#ll\##.###

UPLOAD START	 g01 	 torrents\[####] # ##, ### ## ####(##)\###.###

COMMAND	 rclone move local:"torrents\[####] # ##, ### ## ####(##)\###.###" g01:"TV\TEMP\[####] # ##, ### ## ####(##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ### ####\crawl_info.txt

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\[####] # ##, ### ## ####(##)\###.###

UPLOAD START	 g01 	 torrents\[####] # ##, ### ## ####(##)\crawl_info.txt

COMMAND	 rclone move local:"torrents\[####] # ##, ### ## ####(##)\crawl_info.txt" g01:"TV\TEMP\[####] # ##, ### ## ####(##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\[####] # ##, ### ## ####(##)\crawl_info.txt

UPLOAD START	 g01 	 torrents\[####] # ##, ### ## ####(##)\fanart.jpg

COMMAND	 rclone move local:"torrents\[####] # ##, ### ## ####(##)\fanart.jpg" g01:"TV\TEMP\[####] # ##, ### ## ####(##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\[####] # ##, ### ## ####(##)\fanart.jpg

UPLOAD START	 g01 	 torrents\[####] # ##, ### ## ####(##)\post#r.jpg

COMMAND	 rclone move local:"torrents\[####] # ##, ### ## ####(##)\post#r.jpg" g01:"TV\TEMP\[####] # ##, ### ## ####(##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\[####] # ##, ### ## ####(##)\post#r.jpg

UPLOAD START	 g01 	 torrents\[####] # ##, ### ## ####(##)\#

COMMAND	 rclone move local:"torrents\[####] # ##, ### ## ####(##)\#" g01:"TV\TEMP\[####] # ##, ### ## ####(##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\[####] # ##, ### ## ####(##)\#

UPLOAD START	 g01 	 torrents\### ###! ####\###.###

COMMAND	 rclone move local:"torrents\### ###! ####\###.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\###.###

UPLOAD START	 g01 	 torrents\### ###! ####\###.###

COMMAND	 rclone move local:"torrents\### ###! ####\###.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\###.###

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\##### ### ##\##### ### ## ###.###

UPLOAD START	 g01 	 torrents\####\crawl_info.txt

COMMAND	 rclone move local:"torrents\####\crawl_info.txt" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\crawl_info.txt

UPLOAD START	 g01 	 torrents\####\### ### ## ##.###

COMMAND	 rclone move local:"torrents\####\### ### ## ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\crawl_info.txt

COMMAND	 rclone move local:"torrents\### ###! ####\crawl_info.txt" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\### ### ## ##.###

UPLOAD START	 g01 	 torrents\####\### # ### ##.###

COMMAND	 rclone move local:"torrents\####\### # ### ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ###! ####\crawl_info.txt

UPLOAD START	 g01 	 torrents\### ###! ####\fanart.jpg

COMMAND	 rclone move local:"torrents\### ###! ####\fanart.jpg" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\### # ### ##.###

UPLOAD START	 g01 	 torrents\####\### ### ## ##.###

COMMAND	 rclone move local:"torrents\####\### ### ## ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\fanart.jpg

UPLOAD START	 g01 	 torrents\### ###! ####\post#r.jpg

COMMAND	 rclone move local:"torrents\### ###! ####\post#r.jpg" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\### ### ## ##.###

UPLOAD START	 g01 	 torrents\####\## ## ##.###

COMMAND	 rclone move local:"torrents\####\## ## ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ###! ####\post#r.jpg

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\## ## ##.###

UPLOAD START	 g01 	 torrents\####\## ## ## ##.###

COMMAND	 rclone move local:"torrents\####\## ## ## ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\## ## ## ##.###

UPLOAD START	 g01 	 torrents\####\# ## ## ### ##.###

COMMAND	 rclone move local:"torrents\####\# ## ## ### ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\# ## ## ### ##.###

UPLOAD START	 g01 	 torrents\####\#### #### ##.###

COMMAND	 rclone move local:"torrents\####\#### #### ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\###.###

COMMAND	 rclone move local:"torrents\### ###! ####\###.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\#### #### ##.###

UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\####\### ## ##.###

COMMAND	 rclone move local:"torrents\####\### ## ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\###.###

UPLOAD START	 g01 	 torrents\### ###! ####\##.###

COMMAND	 rclone move local:"torrents\### ###! ####\##.###" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\####\### ## ##.###

UPLOAD START	 g01 	 torrents\####\### ### ## ##.###

COMMAND	 rclone move local:"torrents\####\### ### ## ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\-####- ###\### TV ##### -## # ####- - #### ##### ##.###

UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\-####- ###\#### #### ## - #### ### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\#### #### ## - #### ### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.###.##.###
UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\##.###

UPLOAD START	 g01 	 torrents\### ###! ####\#

COMMAND	 rclone move local:"torrents\### ###! ####\#" g01:"TV\TEMP\### ###! ####" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD DONE		 g01 	 torrents\-####- ###\#### #### ## - #### ### ##.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD START	 g01 	 torrents\-####- ###\## ### ## ### ### ##### - #### ##### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\## ### ## ### ### ##### - #### ##### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ###! ####\#

UPLOAD START	 g01 	 torrents\##### ##\fanart.jpg

COMMAND	 rclone move local:"torrents\##### ##\fanart.jpg" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\-####- ###\## ### ## ### ### ##### - #### ##### ##.###

UPLOAD START	 g01 	 torrents\-####- ###\#### 힙# ### - #### ### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\#### 힙# ### - #### ### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD DONE		 g01 	 torrents\##### ##\fanart.jpg

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD START	 g01 	 torrents\##### ##\post#r.jpg

COMMAND	 rclone move local:"torrents\##### ##\post#r.jpg" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\-####- ###\#### 힙# ### - #### ### ##.###

UPLOAD START	 g01 	 torrents\-####- ###\## # ### ## # ## - #### ##### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\## # ### ## # ## - #### ##### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\post#r.jpg

UPLOAD START	 g01 	 torrents\##### ##\###.###

COMMAND	 rclone move local:"torrents\##### ##\###.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\-####- ###\## # ### ## # ## - #### ##### ##.###

UPLOAD START	 g01 	 torrents\-####- ###\### TV ##### -## # ####- - #### ##### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\### TV ##### -## # ####- - #### ##### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\###.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\-####- ###\### TV ##### -## # ####- - #### ##### ##.###

UPLOAD START	 g01 	 torrents\-####- ###\### TV ##### #, #, #! - #### ##### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\### TV ##### #, #, #! - #### ##### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\###.###

COMMAND	 rclone move local:"torrents\##### ##\###.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\-####- ###\### TV ##### #, #, #! - #### ##### ##.###

UPLOAD START	 g01 	 torrents\-####- ###\### ### ### ######### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\### ### ### ######### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\###.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\-####- ###\### ### ### ######### ##.###

UPLOAD START	 g01 	 torrents\-####- ###\#### # ### ###- - ##### ##.###

COMMAND	 rclone move local:"torrents\-####- ###\#### # ### ###- - ##### ##.###" g01:"TV\TEMP\-####- ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\-####- ###\#### # ### ###- - ##### ##.###

UPLOAD START	 g01 	 torrents\##### ###\#    ## ## - #### ## - ## ### #### # ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ## ## - #### ## - ## ### #### # ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\###.###

COMMAND	 rclone move local:"torrents\##### ##\###.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\###.###

UPLOAD START	 g01 	 torrents\##### ##\###.###

COMMAND	 rclone move local:"torrents\##### ##\###.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\###.###

UPLOAD START	 g01 	 torrents\##### ##\###.###

COMMAND	 rclone move local:"torrents\##### ##\###.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ###\#####.###

UPLOAD START	 g01 	 torrents\### ###\#####.###

COMMAND	 rclone move local:"torrents\### ###\#####.###" g01:"TV\TEMP\### ###" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\###.###

UPLOAD START	 g01 	 torrents\##### ##\###.###

COMMAND	 rclone move local:"torrents\##### ##\###.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\###.###

UPLOAD START	 g01 	 torrents\##### ##\###.###

COMMAND	 rclone move local:"torrents\##### ##\###.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\###.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\crawl_info.txt

COMMAND	 rclone move local:"torrents\##### ##\crawl_info.txt" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\crawl_info.txt

UPLOAD START	 g01 	 torrents\##### ##\###.###

COMMAND	 rclone move local:"torrents\##### ##\###.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\###.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\##.###

COMMAND	 rclone move local:"torrents\##### ##\##.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\##.###

UPLOAD START	 g01 	 torrents\##### ##\#

COMMAND	 rclone move local:"torrents\##### ##\#" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ##\#

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\fanart.jpg

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\fanart.jpg" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\##### ###\#    ## ## - #### ## - ## ### #### # ###.###

UPLOAD START	 g01 	 torrents\##### ###\#    ### - ### ## - ### ## - ### ## ## ##.###

COMMAND	 rclone move local:"torrents\##### ###\#    ### - ### ## - ### ## - ### ## ## ##.###" g01:"TV\TEMP\##### ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\fanart.jpg

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\post#r.jpg

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\post#r.jpg" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\post#r.jpg

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\## #### ####\##.###

COMMAND	 rclone move local:"torrents\## #### ####\##.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\##.###

UPLOAD START	 g01 	 torrents\## #### ####\crawl_info.txt

COMMAND	 rclone move local:"torrents\## #### ####\crawl_info.txt" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\## #### ####\crawl_info.txt

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\### ### ####\####.###

COMMAND	 rclone move local:"torrents\### ### ####\####.###" g01:"TV\TEMP\### ### ####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD DONE		 g01 	 torrents\####\### ### ## ##.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD START	 g01 	 torrents\####\# ## ## ### ##.###

COMMAND	 rclone move local:"torrents\####\# ## ## ### ##.###" g01:"TV\TEMP\####" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\##### ###\#    ### - ### ## - ### ## - ### ## ## ##.###

UPLOAD START	 g01 	 torrents\##### ###\#    ## #-# - ## #-# ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ## #-# - ## #-# ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\#

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\#" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\#

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\crawl_info.txt

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\crawl_info.txt" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\crawl_info.txt

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\###.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\###.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\###.###

UPLOAD START	 g01 	 torrents\### ## Grand# Road (##)\##.###

COMMAND	 rclone move local:"torrents\### ## Grand# Road (##)\##.###" g01:"TV\TEMP\### ## Grand# Road (##)" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ## Grand# Road (##)\##.###

UPLOAD START	 g01 	 torrents\### ##\##.###

COMMAND	 rclone move local:"torrents\### ##\##.###" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\##.###

UPLOAD START	 g01 	 torrents\### ##\##.###

COMMAND	 rclone move local:"torrents\### ##\##.###" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\##### ###\#    ## #-# - ## #-# ###.###

UPLOAD START	 g01 	 torrents\##### ###\#    ### ### - ## ## # #### - ## ## ### #### ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ### ### - ## ## # #### - ## ## ### #### ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\### ##\##.###

UPLOAD START	 g01 	 torrents\### ##\##.###

COMMAND	 rclone move local:"torrents\### ##\##.###" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\##.###

UPLOAD START	 g01 	 torrents\### ##\##.###

COMMAND	 rclone move local:"torrents\### ##\##.###" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\##.###

UPLOAD START	 g01 	 torrents\### ##\#

COMMAND	 rclone move local:"torrents\### ##\#" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\#

UPLOAD START	 g01 	 torrents\### ##\fanart.jpg

COMMAND	 rclone move local:"torrents\### ##\fanart.jpg" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\fanart.jpg

UPLOAD START	 g01 	 torrents\### ##\post#r.jpg

COMMAND	 rclone move local:"torrents\### ##\post#r.jpg" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\post#r.jpg

UPLOAD START	 g01 	 torrents\### ##\##.###

COMMAND	 rclone move local:"torrents\### ##\##.###" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\##.###

UPLOAD START	 g01 	 torrents\### ##\##.###

COMMAND	 rclone move local:"torrents\### ##\##.###" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\##.###

UPLOAD START	 g01 	 torrents\### ##\crawl_info.txt

COMMAND	 rclone move local:"torrents\### ##\crawl_info.txt" g01:"TV\TEMP\### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\### ##\crawl_info.txt

UPLOAD START	 g01 	 torrents\##### ##\fanart.jpg

COMMAND	 rclone move local:"torrents\##### ##\fanart.jpg" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\###\### ###.###

UPLOAD START	 g01 	 torrents\###\### ###.###

COMMAND	 rclone move local:"torrents\###\### ###.###" g01:"TV\TEMP\###" --bind ###.###.###.#
UPLOAD DONE		 g01 	 torrents\##### ##\fanart.jpg

UPLOAD START	 g01 	 torrents\##### ##\post#r.jpg

COMMAND	 rclone move local:"torrents\##### ##\post#r.jpg" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\##### ##\post#r.jpg

UPLOAD START	 g01 	 torrents\##### ##\#

COMMAND	 rclone move local:"torrents\##### ##\#" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\##### ##\#

UPLOAD START	 g01 	 torrents\##### ##\crawl_info.txt

COMMAND	 rclone move local:"torrents\##### ##\crawl_info.txt" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\##### ##\crawl_info.txt

UPLOAD START	 g01 	 torrents\##### ##\####.###

COMMAND	 rclone move local:"torrents\##### ##\####.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\##### ###\#    ### ### - ## ## # #### - ## ## ### #### ###.###

UPLOAD START	 g01 	 torrents\##### ###\#    ###### - ### ## ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ###### - ### ## ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\####\# ## ## ### ##.###

UPLOAD DONE		 g01 	 torrents\### ### ####\####.###

UPLOAD START	 g01 	 torrents\####\### ### ## ##.###

COMMAND	 rclone move local:"torrents\####\### ### ## ##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\## #### ####\###.###

COMMAND	 rclone move local:"torrents\## #### ####\###.###" g01:"TV\TEMP\## #### ####" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\### ###\#####.###

UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\### ###\####.###

COMMAND	 rclone move local:"torrents\### ###\####.###" g01:"TV\TEMP\### ###" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\#### #\crawl_info.txt

COMMAND	 rclone move local:"torrents\#### #\crawl_info.txt" g01:"TV\TEMP\#### #" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\#### #\crawl_info.txt

UPLOAD START	 g01 	 torrents\#### #\fanart.jpg

COMMAND	 rclone move local:"torrents\#### #\fanart.jpg" g01:"TV\TEMP\#### #" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\#### #\fanart.jpg

UPLOAD START	 g01 	 torrents\#### #\post#r.jpg

COMMAND	 rclone move local:"torrents\#### #\post#r.jpg" g01:"TV\TEMP\#### #" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\##### ###\#    ###### - ### ## ###.###

UPLOAD DONE		 g01 	 torrents\#### #\post#r.jpg

UPLOAD START	 g01 	 torrents\##### ###\#    ## #-# - ## #-# ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ## #-# - ## #-# ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\##### ###\#    ## #-# - ## #-# ###.###

UPLOAD START	 g01 	 torrents\##### ###\#    ## ## - ## ### - #### ##.###

COMMAND	 rclone move local:"torrents\##### ###\#    ## ## - ## ### - #### ##.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\##.###

COMMAND	 rclone move local:"torrents\###\##.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\##.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\##### ###\#    ## ## - ## ### - #### ##.###

UPLOAD START	 g01 	 torrents\##### ###\#    VR# ## ## - ### ## - ## ## ## ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    VR# ## ## - ### ## - ## ## ## ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\####\### ### ## ##.###

UPLOAD START	 g01 	 torrents\####\#### #### ##.###

COMMAND	 rclone move local:"torrents\####\#### #### ##.###" g01:"TV\TEMP\####" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\##.###

COMMAND	 rclone move local:"torrents\###\##.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\##.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\##### ###\#    VR# ## ## - ### ## - ## ## ## ###.###

UPLOAD START	 g01 	 torrents\##### ###\#    ## #-# - ## #-# - ## #-## ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ## #-# - ## #-# - ## #-## ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\## #### ####\###.###

UPLOAD START	 g01 	 torrents\###### ### ##\###.###

COMMAND	 rclone move local:"torrents\###### ### ##\###.###" g01:"TV\TEMP\###### ### ##" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\##.###

COMMAND	 rclone move local:"torrents\###\##.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\##.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\##### ###\#    ## #-# - ## #-# - ## #-## ###.###

UPLOAD START	 g01 	 torrents\##### ###\crawl_info.txt

COMMAND	 rclone move local:"torrents\##### ###\crawl_info.txt" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\##### ###\crawl_info.txt

UPLOAD START	 g01 	 torrents\##### ###\#    VR# ## ## - ### ## - ## ## ## ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    VR# ## ## - ### ## - ## ## ## ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\##### ###\#    VR# ## ## - ### ## - ## ## ## ###.###

UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\##### ###\#    #### ## - ## ### #### - ### ## ##.###

COMMAND	 rclone move local:"torrents\##### ###\#    #### ## - ## ### #### - ### ## ##.###" g01:"TV\TEMP\##### ###" --bind ###.###.###.##
UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD DONE		 g01 	 torrents\##### ###\#    #### ## - ## ### #### - ### ## ##.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD START	 g01 	 torrents\##### ###\#    ### ## ## - ### ## ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ### ## ## - ### ## ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD DONE		 g01 	 torrents\##### ###\#    ### ## ## - ### ## ###.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD START	 g01 	 torrents\##### ###\#    ## ### ## - ## #### ##.###

COMMAND	 rclone move local:"torrents\##### ###\#    ## ### ## - ## #### ##.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\##### ##\####.###

UPLOAD START	 g01 	 torrents\##### ##\####.###

COMMAND	 rclone move local:"torrents\##### ##\####.###" g01:"TV\TEMP\##### ##" --bind ###.###.#.#
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\#.###

COMMAND	 rclone move local:"torrents\#### #\#.###" g01:"TV\TEMP\#### #" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\#.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD DONE		 g01 	 torrents\####\#### #### ##.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\####\### # ### ##.###

COMMAND	 rclone move local:"torrents\####\### # ### ##.###" g01:"TV\TEMP\####" --bind ###.##.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\###### ### ##\###.###

UPLOAD START	 g01 	 torrents\###### ### ##\###.###

COMMAND	 rclone move local:"torrents\###### ### ##\###.###" g01:"TV\TEMP\###### ### ##" --bind ###.###.##.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\###.###

COMMAND	 rclone move local:"torrents\###\###.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\###\###.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\##### ###\#    ## ### ## - ## #### ##.###

UPLOAD START	 g01 	 torrents\##### ###\#    ## ### ## - ## #### ##.###

COMMAND	 rclone move local:"torrents\##### ###\#    ## ### ## - ## #### ##.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.#.##
UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\##### ###\#    ## ### ## - ## #### ##.###

UPLOAD START	 g01 	 torrents\##### ###\#    ### ## - ## ## ## - ### ##, ## ## ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ### ## - ## ## ## - ### ##, ## ## ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\##### ###\#    ### ## - ## ## ## - ### ##, ## ## ###.###

UPLOAD START	 g01 	 torrents\##### ###\#    ###### - ### ## ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ###### - ### ## ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.#.##
UPLOAD DONE		 g01 	 torrents\##### ###\#    ###### - ### ## ###.###

UPLOAD START	 g01 	 torrents\##### ###\#    ## ## - #### ## - ## ### #### # ###.###

COMMAND	 rclone move local:"torrents\##### ###\#    ## ## - #### ## - ## ### #### # ###.###" g01:"TV\TEMP\##### ###" --bind ###.##.###.###
UPLOAD DONE		 g01 	 torrents\#### #\####.###

UPLOAD START	 g01 	 torrents\#### #\####.###

COMMAND	 rclone move local:"torrents\#### #\####.###" g01:"TV\TEMP\#### #" --bind ###.###.###.##
UPLOAD DONE		 g01 	 torrents\###\####.###

UPLOAD START	 g01 	 torrents\###\####.###

COMMAND	 rclone move local:"torrents\###\####.###" g01:"TV\TEMP\###" --bind ###.###.#.##

