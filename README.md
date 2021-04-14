# Project 1: ETL Data Processor 

The Nashville housing data set used in this project is from kaggle and can be found: https://www.kaggle.com/tmthyjames/nashville-housing-data. Almost half of the observations do not list key home features such as total value of home or any other features and were therefore removed in the data cleaning process.

## Installation

Use the package manager pip to install pandas:

```bash
pip install pandas
```

## Contents of Project

The files above consist of the Nashville housing data set from kaggle, the python script used in the ETL pipeline, the requirements.txt and the dockerfile. Simply run the housing_ETL.py script and two new files, a cleaned csv and json file, will be saved to the directory. Details of the data cleaning steps are described below, including an addional column for further analysis.

## Brief Summary of Data Ingestion

The original data set contained 56,636 records and 31 columns. The data cleaning process included removing unnecessary (image column) and duplicated columns, as well as removing records that contained mostly NA values. Records were removed if they did not have a number listed under for the 'Total Value' column. This process left the data set with 26,017 records and 28 columns. Another column was added named '80/20 Rule' which calculated the ratio of the land value over the total value of the home. If the number fell between 0.15 and 0.25 then we can say the ho passes the 80/20 Rule of land/building value. The final step in the ETL pipeline was to convert the cleaned csv file to a json file. 
