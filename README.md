# PyCrowdTangle
A Python Wrapper To Retrieve Data From The CrowdTangle API

https://github.com/CrowdTangle/API


## Install

```
pip install PyCrowdTangle
```
### Update
```
pip install PyCrowdTangle -U
```
## Usage

### ct_get_posts
```python
import PyCrowdTangle as pct

#retrieve data from CrowdTangle
# get the api_token from https://apps.crowdtangle.com/
# you can locate your API token via your crowdtangle dashboard
# under Settings > API Access.

data = pct.ct_get_posts(api_token="AKJHXDFYTGEBKRJ6535")

import pandas as pd

df = pd.DataFrame(data['result']['posts'])

#show results
df.head()
```
### ct_get_links
```python
import PyCrowdTangle as pct

#retrieve data from CrowdTangle
# get the api_token from https://apps.crowdtangle.com/
# you can locate your API token via your crowdtangle dashboard
# under Settings > API Access.

data = pct.ct_get_links(link= 'http://www.queenonline.com/', platforms='facebook',
                     start_date='2019-01-01',api_token="AKJHXDFYTGEBKRJ6535")

import pandas as pd

df = pd.DataFrame(data['result']['posts'])

#show results
df.head()
```

### ct_get_lists
```python
import PyCrowdTangle as pct

#retrieve data from CrowdTangle
# get the api_token from https://apps.crowdtangle.com/
# you can locate your API token via your crowdtangle dashboard
# under Settings > API Access.

data = pct.ct_get_lists(api_token="AKJHXDFYTGEBKRJ6535")

#show results
print(data)
```