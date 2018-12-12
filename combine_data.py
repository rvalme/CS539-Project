import pandas as pd
import numpy as np

def Import_DataSets(files):
    df_list = []

    for file in files:
        df = pd.read_csv(file, dtype="str")
        df_list.append(df)

    return df_list



def Merge_Values(store_count, us_census):

    #us_census['Count'] = 0

    print(us_census)
    print(store_count)

    combined_df = pd.merge(us_census, store_count, on='Geography', how='outer')
    combined_df.Count.fillna(value=0, inplace=True)

    print(combined_df)

    combined_df["ZIP1"]  = combined_df.Geography.str[0]
    combined_df["ZIP23"] = combined_df.Geography.str[1:3]
    combined_df["ZIP45"] = combined_df.Geography.str[3:]

    combined_df.to_csv("combined_df.csv", sep=',', index = False, )

    print(combined_df.head())


def Main():
    store_count_files = ["count.csv"]
    us_census_files = ["Cleaned_USCensus_2016.csv"]

    store_count_datasets = Import_DataSets(store_count_files)
    us_census_datasets = Import_DataSets(us_census_files)

    Merge_Values(store_count_datasets[0], us_census_datasets[0])


Main()