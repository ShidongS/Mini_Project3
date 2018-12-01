# encoding: utf-8
# Author - Shidong Sun
import tweepy #https://github.com/tweepy/tweepy
import json
import urllib.request
import os
from PIL import Image
from pymongo import MongoClient
import io
from google.cloud import vision
from google.cloud.vision import types
import mysql.connector
# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets():
    # Pass in the username of the account you want to download
    screen_name=input('Please input the account name you want to download:')
    # API authoriazation
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        client = vision.ImageAnnotatorClient()
    except:
        print('Google authentification error')
        return
    # setup the database
    cnx = mysql.connector.connect(user='username',
                              password='password',
                              database='Mini3')
    cursor = cnx.cursor()
    add_tag = ("INSERT IGNORE INTO tags "
                "(tag_no, tag_name) "
                "VALUES (%s, %s)")
    add_link = ("INSERT IGNORE INTO link "
                    "(pic_no, tag_no) "
                    "VALUES (%s, %s)")
    add_pic = ("INSERT IGNORE INTO pictures "
               "(pic_no, url, account_name) "
               "VALUES (%s, %s, %s)")

    alltweets = []

    # Make first request of getting tweets, get 10 new tweets and add them to the tweet list
    try:    
        new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    except:
        print('account number not found')  
        return
    alltweets.extend(new_tweets)   
    # Prevent some extreme conditions that there is no tweet in this account 
    B=int(input('Please input the number of tweets you want to scan(from 20 to 3000):'))
    while(B<20 or B>3000):
        B=int(input('Number not accepted, please retry:'))
    if(alltweets==[]):
        print('No tweet found') 
        return 
    oldest = alltweets[-1].id - 1

    # Repeat the same progress if the first request is successful
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        # Shut the progress when meeting the user's requirement
        if(len(alltweets) >= B):
            break
    media_files = set()

    # Select media file url from all tweets and save them
    # Credit to https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
    for status in alltweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])

    # Prevent no-image situiation
    if(media_files==set([])):
        print("No pictures available")
        return
    i=1
    tag=[]

    # Download all images into your computer and save them with standard names
    folder=os.getcwd()+'/picture/'
    if not os.path.exists(folder):
        os.makedirs(folder)
    for media_file in media_files:
        urllib.request.urlretrieve(media_file,folder+'%04d'%(i))
        img = Image.open(folder+'%04d'%(i))
        img = img.convert('RGB')
        img.save(folder+'%04d'%(i)+'.jpg')
        os.remove(folder+'%04d'%(i))
        file_name = os.path.join(os.path.dirname(__file__),folder+'%04d'%(i)+'.jpg')

        # Send picture to Google API
        # Load the image into memory
        # The following 6 line credit to Google quick start
        with io.open(file_name, 'rb') as image_file:
                content = image_file.read()
        image = types.Image(content=content)
        # Run label detection on the image file
        try:
             response = client.label_detection(image=image)
        except:
            print('Google API not responding')
            return
        labels = response.label_annotations
        for label in labels:
            tag.append(label.description)
        print(tag)

        # add information into database
        # to table 'picture'
        cursor.execute("SELECT MAX(pic_no) FROM pictures")
        last_pic_no = cursor.fetchall()[0][0]
        if last_pic_no == None:
            last_pic_no = 0
        pic_data = (last_pic_no+1, media_file, screen_name)
        cursor.execute(add_pic, pic_data)
        # to table 'tags'
        for element in tag:
            cursor.execute("SELECT MAX(tag_no) FROM tags")
            last_tag_no = cursor.fetchall()[0][0]
            if last_tag_no == None:
                last_tag_no = 0
            tag_data = (last_tag_no+1, element)
            cursor.execute(add_tag, tag_data)
        # to table 'link'
            cursor.execute("SELECT tag_no FROM tags WHERE tag_name = '"+element+"'")
            link_tag_no = cursor.fetchall()[0][0]
            link_data = (last_pic_no+1, link_tag_no)
            cursor.execute(add_link, link_data)
        cnx.commit()
        tag.clear()
        i+=1
    print("Finish")
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    get_all_tweets()
