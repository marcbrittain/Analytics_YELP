from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json
import pandas as pd
import numpy as np


#######################################################################################################
#                                         Restaurant Rating Finder                                    #
#                                         Created By: Marc Brittain                                   #
#######################################################################################################
# This tool was created to help the functionality of the current YELP Api. Currently there are negative 
# reviews regarding the API's ability to provide information so this should be able to help users access
# the information in an easy to use format. This current program determines only the restaurant 
# information for a city, but more features are going to be released as well as different analytics that
# can be run from the data. If you have any comments or suggestions, please feel free to email me at
# mwb7302@uncw.edu
########################################################################################################



def create_business_lists(response, business_list, ratings_list, phone_list):
    """loop through the businesses in a particular offset window and update data lists
        
    args:
        response      (obj):  business information for 20 restaurants
        business_list (list): list containing restaurant names
        ratings_list  (list): list containing rating values
        phone_list    (list): list containing phone numbers
        
    returns:
        None            
    """

    for i in range(len(response.businesses)):
        business_name = response.businesses[i].name 
        business_rating = response.businesses[i].rating
        business_phone = response.businesses[i].phone
        
        business_list.append(business_name)
        ratings_list.append(business_rating)
        phone_list.append(business_phone)

######################################################################################################



def grab_restaurants(city, offset):
    """grabs business information for the input city
    
    args:
        city   (str): the input city
        offset (int): input value to change the search window for the city
        
    returns: 
        20 restaurants based on the search window for a given city
    """
    
    # set up api call with given keys
    # I followed Yelp's advice to store api information in a json file for privacy
    
    with io.open('config_secret.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)
        
    # set parameters to search for restuarants in a given offset window
        params = {
        'term': 'restaurant',
        'offset': offset
        }


    return client.search(city, **params)

#####################################################################################################



def create_dataFrames(business_list, ratings_list, phone_list, city):
    """creates a dataframe combining the different data lists
    
    args:
        business_list (list): list of restaurant names
        ratings_list  (list): list of ratings
        phone_list    (list): list of phone numbers
        
    returns:
        a dataframe joining the restuarant names, ratings, and phone numbers    
    """
    
    business_df = pd.DataFrame(business_list)
    ratings_df = pd.DataFrame(ratings_list)
    phone_df = pd.DataFrame(phone_list)
    
    business_df.rename(columns={0: city[0].upper()+city[1:]+' Restaurants'}, inplace=True)
    ratings_df.rename(columns={0: city[0].upper()+city[1:]+' Ratings'}, inplace=True)
    phone_df.rename(columns={0: city[0].upper()+city[1:]+' Phone Number'}, inplace=True)
    
    business_df = business_df.join(ratings_df)
    business_df = business_df.join(phone_df)
    
    return business_df

######################################################################################################


def ratingThreshold(df, city, r, r_type=0):
    """Determines the restaurant information for a given city with ratings above or below a given threshold
    
    args:
        df   (dataframe): input restaurant dataframe
        city (str):       input city
        r    (float):     input rating threshold
        r_type (int):     specify to return values above or below threshold. 1 for below, default = 0
    returns:
        dataframe with restaurant information above rating threshold
    """
    
    city = city[0].upper()+city[1:].lower()    
    index = []
    index_value = 0
    for i in df[str(city)+' Ratings']:
        if r_type == 0:
            if i >= r:
                index.append(index_value)
        if r_type == 1:
            if i <= r:
                index.append(index_value)
        index_value += 1
    name = []
    phone = []
    rating = []
    
    for value in index:
        name.append(df[city+' Restaurants'][value])
        phone.append(df[city+' Phone Number'][value])
        rating.append(df[city+' Ratings'][value])
    
    name_df = pd.DataFrame(name)
    phone_df = pd.DataFrame(phone)
    rating_df = pd.DataFrame(rating)
    
    name_df.rename(columns={0 : city+' Restaurants'}, inplace=True)
    phone_df.rename(columns={0 : city+' Phone Number'}, inplace=True)
    rating_df.rename(columns={0 : city+' Ratings'}, inplace=True)
    
    name_df = name_df.join(rating_df)
    name_df = name_df.join(phone_df)
    
    return name_df

#####################################################################################################


def isCustomer(l, city):
    
    """[business tool] Determines the restaurants in the given location that are customers
    
    args:
        l (list):  input list of customers for a city
        city (df): input city to examine
    returns:
    
        dataframe of customers in a given city
    """
    
    index = []
    for line in l:
        names = df[city+' Restaurants']
        count = 0
        for i in names:
            if line == i:
                index.append(count)
            count += 1
    for value in count:
        customer_phone.append(df[city+' Phone Number'][value])
        customer_name.append(df[city+' Restaurants'][value])
        customer_rating.append(df[city+' Ratings'][value])
    
    phone_df = pd.DataFrame(customer_phone)
    name_df = pd.DataFrame(customer_name)
    rating_df = pd.DataFrame(customer_rating)
    
    phone_df.rename(columns={0: 'Customer Phone'}, inplace=True)
    name_df.rename(columns={0: 'Customer Name'}, inplace=True)
    rating_df.rename(columns={0: 'Customer Rating'}, inplace=True)
    
    name_df = name_df.join(rating_df)
    name_df = name_df.join(phone_df)
    
    return name_df

#####################################################################################################

def restaurant_ratings_city(r=None, r_type=None):
    
    """Determines the ratings and restaurants for a given city
    
    args:
        r (int):      rating threshold; default: None
        r_type (int): determines to threshold above or below the value r; default: None
    
    returns:
        dataframe with the input citites and restaurants
    """
        
    main = pd.DataFrame()
    s = raw_input("Enter City Names (comma separated, no spaces): ")
    s = s.lower()
    s = s.split(',')
    for city in s:
        
        offset = 0
        business_list = []
        ratings_list = []
        phone_list = []
        
        total = grab_restaurants(city, offset).total
        
        if total > 1000:
            total = 1000
            
        while offset < total:
                        
            response = grab_restaurants(city, offset)

            create_business_lists(response, business_list, ratings_list, phone_list)
                
            offset += 20
            
        df = create_dataFrames(business_list, ratings_list, phone_list, city)
        
        if main.empty:
            main = df
        else:
            main = main.join(df)
    if r_type == 0 or r_type == 1:
        city_Threshold = raw_input("Enter City to Threshold: ")
        main = ratingThreshold(main, city, r, r_type)
    
    return main

########################################################################################################