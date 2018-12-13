# CS539-Project

### Instructions ###
To run all of our scripts, you will need to download our cleaned 2016 US Census data file from: https://www.dropbox.com/s/rh7xojgbkqbt5dh/2017_USCensus_Cleaned.csv?dl=0 and keep it in the same directory as our XGBoost Code.
Our script will concatenate the predicted values from XGBoost to the original US Census dataset.

Download format_data.py and combine_data.py from this GitHub branch. Put both these files in the same directory as as the uncleaned data files and run them both. These scripts will produce the correct output you need to run the XGBoost Script.

If you want to work with our original and uncleaned datasets, you can download the US Census data and the original Starbucks store list directly from the source by clicking on the two links directly below.

### Original Data Sources ###
Starbucks 2017 Store List: https://www.dropbox.com/s/4ltmagcpcsfkbvc/Cleaned_Starbucks_2017.csv?dl=0
<br />US Census Data Direct Link: https://www.census.gov/programs-surveys/acs/about.html


## Prerequisite For Linear Regression and Neural Network ##
This python script predicts the number of starbucks in a zip code using US demographic census data and past starbucks locations. This script requries python3, numpy, pandas, sklearn and an input file named Combined_Count.csv, which contains the zip codes and their corresponding demographic data and number of starbucks open.

### Code ###
To find the optimal performance when predicting the number of stores in a zip code, our approach ranks the features in order of importance and uses different machine learning algorithms to make predictions. The features extraction is done by by decision_tree.py and hardcoded in this script.

This script incrementally takes the most relevant features as input to make predictions; with the first run only using the feature with the most information gain, the second run using two features with the most information gain, and so on.

The script trains on 2012 and 2013 starbucks locations and census data and predicts 2017 starbucks locations using 2017 census data

### To run this code type ##
`python lr_nn.py ml_option`
The ml_option can be 1 or 2 or 3, 1 for XGBoost, 2 for neural network, 3 for linear regression. The script will output the accuracy of the predictions to the standard output and save the predictions to an excel file.


