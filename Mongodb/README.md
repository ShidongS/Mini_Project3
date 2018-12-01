# Project-Mongo
This project is based on Twitter API, Google API and Mongodb. These things must be installed before running this project.
pymongo module is also needed, which can be installed by the following command: </br>
`pip3 install pymongo`
This project is written by Python3.
Before ruuning the project, mongodb must be installed and started properly, otherwise it will report an error saying connection refused.
The mongo_link.py file is the main file which can search and download images from Twitter API and store the imformation of account name, url and tags into a mongodb database called Mini3.
The mongo_search file provides 3 functions: Print all account names by their image numbers, Print all tags by their popularity, and search a tag and find which account(s) have it. All the founctions can be used by following the instuctions inside the program.
Search must be used after the main file or it cannot link to the database and report a connection failure.
