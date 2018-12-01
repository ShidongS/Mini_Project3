# Project-Mysql
This project is based on Twitter API, Google API and Mysql. These things must be installed before running this project.
pymongo module is also needed, which can be installed by the following command: </br>
`pip3 install mysql-connector`</br>
This project is written by Python3.</br>
Before ruuning the project, mysql must be installed and started properly, otherwise it will report an error saying connection failure.</br>
The create_database.py is aimed at creating a database called Mini3 and 3 tables named pictures, link and tags. The pictures table stores account name and url, the tags table stores all the tags that appeared, and the link table links 2 tables together. Considering that one picture may contain many tags and one tag may apply to more than one picture, this way of storing information is better than storing them directly into the database.</br>
The mysql_link.py file is the main file which can search and download images from Twitter API and store the imformation into database Mini3.</br>
The mongo_search file provides 3 functions: Print all account names by their image numbers, Print all tags by their popularity, and search a tag and find which account(s) have it. All the founctions can be used by following the instuctions inside the program.</br>
Create database should be done at first, or the other 2 programs cannot find the proper database and fail to connect. Once the database is created, it will not be deleted unless you intentionally do it.</br>
Search must be used after the main file or it cannot link to the database and report a connection failure.</br>
The password and username written in the 3 programs should be switched to your own local ones.
