# PyCrowdTangle
A Python Wrapper To Retrieve Data From The CrowdTangle API

https://github.com/CrowdTangle/API

## Usage

``` python
import PyCrowdTangle as pct

#retrieve data from CrowdTangle
# get the api_token from https://apps.crowdtangle.com/

data = pct.ct_get_posts(api_token="AKJHXDFYTGEBKRJ6535")

import pandas as pd

df = pd.DataFrame(data['result']['posts'])

#show results
df.head()
```