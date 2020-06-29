#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def ct_get_links(link, platforms='facebook', count=100, start_date="", end_date="", api_token=""):
    """ Retrieve a set of posts matching a certain link.

    Args:
        link ([type]): [description]
        platforms (str, optional): The platforms from which to retrieve links. This value can be comma-separated.
                                   options: facebook, instagram, reddit. Defaults to 'facebook'.
        count (int, optional): The number of posts to return. Defaults to 100. options [1-100]
        start_date (str, optional): The earliest date at which a post could be posted. Time zone is UTC. 
                                    Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” 
                                    (defaults to time 00:00:00).
        end_date (str, optional):  The latest date at which a post could be posted.
                                  Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss”
                                  or “yyyy-mm-dd” (defaults to time 00:00:00).
                                  Defaults to "now".
        api_token (str, optional): you can locate your API token via your crowdtangle dashboard
                                   under Settings > API Access.

    Raises:
        ValueError: "link was empty"
        ValueError: "api_token variable is empty"

    Returns:
        [dict]: The Response contains both a status code and a result. The status will always
                be 200 if there is no error. The result contains an array of post objects and
                a pagination object with URLs for both the next and previous page, if they exist
    
    Example:
        ct_get_links(link= 'http://www.queenonline.com/', platforms='facebook',
                     start_date='2019-01-01',api_token="AKJHXDFYTGEBKRJ6535")
    """

    # api-endpoint
    URL_BASE = "https://api.crowdtangle.com/links"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'link': link, 'count': count,
              'token': api_token, 'platforms': platforms}

    # add params parameters
    if start_date:
        PARAMS['startDate'] = start_date
    if start_date:
        PARAMS['endDate'] = end_date

    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    # status = r.status_code
    return r.json()


def ct_get_posts(count=100, start_date="", end_date="", api_token=""):
    """Retrieve a set of posts for the given parameters get post from crowdtangle 

    Args:
        count (int, optional): The number of posts to return. Defaults to 100. options [1-100]
        start_date (str, optional): The earliest date at which a post could be posted. Time zone is UTC. 
                                    Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” 
                                    (defaults to time 00:00:00).
        end_date (str, optional): The latest date at which a post could be posted.
                                  Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss”
                                  or “yyyy-mm-dd” (defaults to time 00:00:00).
                                  Defaults to "now".
        api_token (str, optional): you can locate your API token via your crowdtangle dashboard
                                   under Settings > API Access.
    Returns:
        [dict]: The Response contains both a status code and a result. The status will always
                be 200 if there is no error. The result contains an array of post objects and
                a pagination object with URLs for both the next and previous page, if they exist

    Example:
        ct_get_posts(api_token="AKJHXDFYTGEBKRJ6535")                    
    """
    
    # api-endpoint
    URL_BASE = "https://api.crowdtangle.com/posts"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'count': count, 'token': api_token}

    # add params parameters
    if start_date:
        PARAMS['startDate'] = start_date
    if start_date:
        PARAMS['endDate'] = end_date

    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    # status = r.status_code
    return r.json()

def ct_get_lists(api_token=""):
    """Retrieve the lists, saved searches and saved post lists of the dashboard associated with the token sent in

    Args:
        api_token (str, optional): you can locate your API token via your crowdtangle dashboard
                                   under Settings > API Access.
    Returns:
        [dict]: The Response contains both a status code and a result. The status will always
                be 200 if there is no error. The result contains an array of a lists objects

    Example:
        ct_get_lists(api_token="AKJHXDFYTGEBKRJ6535")                    
    """
    
    # api-endpoint
    URL_BASE = "https://api.crowdtangle.com/lists"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'token': api_token}

    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    # status = r.status_code
    return r.json()    