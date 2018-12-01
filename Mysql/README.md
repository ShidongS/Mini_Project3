# Project-learn
This project is composed of 3 programs, which are twitter.py, google.py and link.sh. These programs indicate their function by their names, while some of the picture processing and video merging program lies in google.py and link.sh. This project only works in Linux. The way to run this project is to download all 3 files, open the terminal in the download path and type in './link.sh' and everything is done. This program would scan 50 tweets and download pictures for now. More functions are being added.


2018.9.18 update: now you can type in the acount name and select how many tweets to scan now. It will only work the right account name, otherwise an error will occur. There are more updates including creating new folders to ensure that this project will work on everyone's computer as long as you have the key. Please use your own API key to run this project and don't forget to change the path of google key in link.sh.


2018.9.19 update: The way how this project works is as follows: 1. Enable the twitter API by typing in keys. 2. Download tweets from the account to local computer. 3. Scan all these tweets and select tweet url with media files. 4.Download files and save as images(.jpg) to your computer in a certian folder(if there is not, it will create one). 5.Send these images to Google Vision API and get feedback(the Label Library is uesd in this case). 6. Print and save these labels. 7. Resize all images into same size and add all labels to them to create a new series of images. 8. Merge thoes images with labels into one video.

2018.9.20 update: This edition solves the problem of twitter API not responding and PNG cannot transform to JPG problem.


2018.9.22 update: This edition solves the Google API authentification and no responding error
