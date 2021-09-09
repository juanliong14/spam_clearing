import pandas as pd
import datetime

def load_data(path):
    '''
    Function to load csv data and convert 'Date' to datetime object and 
    create 'Tweet_Date' column as date object
    
    path = dataset file location path 

    Author      : Juan L
    Date        : 8 Sept 2021
    '''
    
    #load csv to pandas dataframe
    df = pd.read_csv(path, error_bad_lines=False)

    #convert pandas object to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    #extract date from datetime object
    df['Tweet_Date'] = pd.to_datetime(df['Date'].dt.date)

    return df


def identify_spammers(data,n_spam=10):
    '''
    Function to automatically identify potential spammers and return it on a list
    
    data = the dataset to identify spammers
    n_spam = number of minimum tweets a day to be identified as spammers


    Author      : Juan L
    Date        : 8 Sept 2021
    '''
    import datetime
    
    spammers = []
    date = data['Tweet_Date'].dt.date.min()
    end_date = data['Tweet_Date'].dt.date.max()
    delta = datetime.timedelta(days=1)

    while date <= end_date:
        
        #subset the data for each date 
        df = data[data['Tweet_Date']==str(date)]

        #identify the suspicious author with tweets equal to or more than n_spam
        sus_authors = df.groupby('Author').filter(lambda x: len(x) >= n_spam)['Author'].unique()

        #extend sus_authors to spammers list
        spammers.extend(sus_authors)

        date += delta
    
    #remove duplicates on spammers list 
    spammers = list(dict.fromkeys(spammers))

    if len(spammers) == 0:
        print('There is no potential spammer identified')
    elif len(spammers) == 1:
        print('There is 1 potential spammer identified')
    else:
        print('There are ' + str(len(spammers)) + ' potential spammers identified')

    return spammers

def check_tweet_per_day(data, author):
    '''
    Function to display number of tweet for each day on the dataset from that author
        
    data = the dataset to identify spammers
    n_spam = number of minimum tweets a day to be identified as spammers
    Author      : Juan L
    Date        : 9 Sept 2021
    '''

    print('The number of tweet for each day by ' + str(author))
    data[data['Author']==author]['Tweet_Date'].value_counts().sort_index()