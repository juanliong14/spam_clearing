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