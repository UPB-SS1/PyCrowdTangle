#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# save in a file called api-key.txt file
# your api-key at your proyect folder
try:
    with open("apikey.txt", "r") as file:
        apikey = file.readline()
        api_token = apikey.strip('\n')
except:
    print("api-key.txt not found")


def ct_get_posts(count=100, start_date="", end_date="", api_token=""):
    """Retrieve a set of posts for the given parameters get post from crowdtangle 

    Args:
        count (int, optional): The number of posts to return. Defaults to 100. options [1-100]
        start_date (str, optional): [description]. Defaults to "".
        end_date (str, optional): The latest date at which a post could be posted.
                                  Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss”
                                  or “yyyy-mm-dd” (defaults to time 00:00:00).
                                  Defaults to "now".
        api_token (str, optional): [description]. Defaults to "".

    Returns:
        [dict]: The Response contains both a status code and a result. The status will always
                be 200 if there is no error. The result contains an array of post objects and
                a pagination object with URLs for both the next and previous page, if they exist
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
