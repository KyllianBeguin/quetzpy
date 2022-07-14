import json
import pandas as pd

def open_json(JSON):
    '''
    Open the json file that contains the Twitter data from API
    '''

    # Opening JSON file
    with open(JSON) as f:

        # returns JSON object as a dictionary
        data = json.load(f)

    print("Data extracted from json file")

    return data['data']

def json_to_dataframe(DATA):
    '''
    Make the dataframe out of the data contained in the json
    '''

    # Get the columns for the dataframe
    columns_df = list(DATA[0].keys())

    # Aggregate the data and store it to another dictionnary
    df_data = [[i[columns_df[j]] for i in DATA] for j in range(len(columns_df))]
    df_dict = {}
    for i in range(len(columns_df)):
        df_dict[columns_df[i]] = df_data[i]

    # Make the dataframe out of the aggregated data
    df = pd.DataFrame(df_dict)

    # Turn the created_at data into a Timestamp data
    df['created_at']= pd.to_datetime(df['created_at'])

    print("Json file transformed into a dataframe")

    return df

def load_dataset(JSON):
    '''
    Load the csv file that contains all the data (= central csv file)
    '''
    try:
        df = pd.read_csv(JSON.replace(".json", ".csv"))
        print("Central dataset loaded")

    except:
        df = 0
        print("Central dataset created")

    return df

def append_and_save_dataset(DF_insert, DF, JSON):
    '''
    Append the new data to the central csv file
    Save de central csv file
    '''

    try:
        DF = pd.concat([DF_insert, DF]).reset_index(drop = True)
        DF.to_csv(JSON.replace("json", "csv"), index = False)

    except:
        DF.to_csv(JSON.replace("json", "csv"), index = False)

    print("Central dataset updated and saved")

    return 
