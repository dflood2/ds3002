#!/usr/bin/env python3

import pandas as pd
import csv
import json

## read in data set 
housing_df = pd.read_csv("Nashville_housing_data_2013_2016.csv")

## remove duplicated columns called Unnamed: 0 and Unnamed: 0.1 and unnecessary columns
housing_df = housing_df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'image'], axis=1)

## remove rows that do not have a total value listed
housing_df = housing_df.dropna(axis=0, subset=['Total Value'])

## 80/20 Rule - Calculating land/total value ratio
housing_df['80/20 Rule'] = housing_df['Land Value']/housing_df['Total Value']

## convert csv to json
housing_df.to_csv('nashville_housing_cleaned.csv')

with open('nashville_housing_cleaned.csv', 'r', encoding='utf8') as csvfile:
    with open('nashville_housing_cleaned.json', 'w', encoding='utf8') as jsonfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        json.dump(list(reader), jsonfile)