#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def ct_get_links(link, platforms='facebook', count=100, start_date='',
                end_date='', include_history='', include_summary='false', 
                offset = 0, sortBy = 'date', api_token=''):
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
        include_history (str, optional): Includes timestep data for growth of each post returned.
                                         Defaults to null (not included). options: 'true'
        include_summary (str, optional): Adds a "summary" section with AccountStatistics for 
                                         each platform that has posted this link. It will look beyond 
                                         the count requested to summarize across the time searched. 
                                         Requires a value for startDate.
                                         Defaults to false. options: 'true' , 'false'

        offset (int, optional):   The number of posts to offset (generally used for pagination). 
                                  Pagination links will also be provided in the response.
                                  Defaults to 0. options >= 0

        sortBy (str, optional):   The method by which to order posts (defaults to the most recent).
                                  If subscriber_count, a startDate is required.
                                  Defaults to 'date'. options: 'subscriber_count' , 'total_interactions'

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
              'token': api_token, 'platforms': platforms, 
              'includeSummary': include_summary , 'offset': offset,
              'sortBy': sortBy
            }

    # add params parameters
    if start_date:
        PARAMS['startDate'] = start_date
    if end_date:
        PARAMS['endDate'] = end_date
    if include_history == 'true':
        PARAMS['includeHistory'] =  'true'

    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    if r.status_code != 200:
        out = r.json()
        print(f"status: {out['status']}")
        print(f"Code error: {out['code']}")
        print(f"Message: {out['message']}")
    else:
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
    if end_date:
        PARAMS['endDate'] = end_date

    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    if r.status_code != 200:
        out = r.json()
        print(f"status: {out['status']}")
        print(f"Code error: {out['code']}")
        print(f"Message: {out['message']}")
    else:
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
    if r.status_code != 200:
        out = r.json()
        print(f"status: {out['status']}")
        print(f"Code error: {out['code']}")
        print(f"Message: {out['message']}")
    else:
        return r.json()