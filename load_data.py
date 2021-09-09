def load_data(path):
    '''
    Function to load csv data and convert 'Date' to datetime object and 
    create 'Tweet_Date' column as date object
    
    path = dataset file location path 

    Author      : Juan L
    Date        : 8 Sept 2021
    '''
    
    import pandas as pd
    import datetime
    
    #load csv to pandas dataframe
    df = pd.read_csv(path, error_bad_lines=False)

    #convert pandas object to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    #extract date from datetime object
    df['Tweet_Date'] = pd.to_datetime(df['Date'].dt.date)

    return df