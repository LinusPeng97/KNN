# KNN

This is a python implementation of KNN writed by Linus Peng 

## Compatibility
The code is tested using scrapy under Ubuntu 16.04 with Python 3.7.

## Training data
This model using data crawled by scrapy from a model website, including their chest, hip and waist measurement, height, weight, cup, shoe size and degree of preference which is labeled by hand according to my preference.

## Pre-processing
Firstly, I use convert_json_to_txt() in preprocess_data.py to convert json format to txt, then process_exception_data() to fill the missing data by average of next two data, by the way, I convert cup A, B, C, D to 10, 12.5, 15, 17.5 respectively. Finally, I use max-min-normalization to process data in normalization().

## Running training
run KNN.py in src package, traing process cost 30 seconds totally. After a century waiting, you can enter some information of a beautiful to get my preference to her!

