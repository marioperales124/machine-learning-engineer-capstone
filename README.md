# machine-learning-engineer-capstone
Capstone Project - Machine Learning Engineer Udacity Nanodegree

## Project

The aim of this project is build a Book recommender system.

All the details are in Capstone-project.pdf

## How to get the data

As I mentioned previously, we are going to use a Goodreads database from this Kaggle Database available in this 
<a href='https://www.kaggle.com/bahramjannesarr/goodreads-book-datasets-10m'>link</a>

The way I read in the project is based on this csvs. If it has changed contact me. <br>

Books data:

* book1-100k.csv
* book100k-200k.csv
* book200k-300k.csv
* book300k-400k.csv
* book400k-500k.csv
* book500k-600k.csv
* book600k-700k.csv
* book700k-800k.csv
* book800k-900k.csv
* book900k-1000k.csv
* book1000k-1100k.csv
* book1100k-1200k.csv
* book1200k-1300k.csv
* book1300k-1400k.csv
* book1400k-1500k.csv
* book1500k-1600k.csv
* book1600k-1700k.csv
* book1700k-1800k.csv
* book1800k-1900k.csv
* book1900k-2000k.csv
* book2000k-3000k.csv
* book3000k-4000k.csv
* book4000k-5000k.csv

Interactions data:

* user_rating_1000_to_2000.csv
* user_rating_2000_to_3000.csv
* user_rating_3000_to_4000.csv
* user_rating_4000_to_5000.csv
* user_rating_5000_to_6000.csv
* user_rating_6000_to_11000.csv

## How to run the project

First clone this repo and download the data. Be sure that the name of the csvs are the same. 
If only the numbers have changed, you only have to change them in config.py

Then run requirements.txt with 

pip install -r requirements.txt

After that, run Project Notebook.ipynb, placed in notebooks folder. All the project should work if you follow the steps

The unique thing you should change is the last cell, change S3 bucket and all the variables you need to change there 