# PyCrowdTangle

A Python Wrapper To Retrieve Data From The [CrowdTangle API](https://github.com/CrowdTangle/API)

## Install

```
pip install PyCrowdTangle
```
### Update
```
pip install PyCrowdTangle -U
```
## Example

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UPB-SS1/PyCrowdTangle/blob/master/examples/pycrowdtangle_example.ipynb)

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


## Acknowledgements

CooRnet has been developed as part of the project [Social Media Behaviour](https://upb-ss1.github.io/) research project activities.

The project is supported by a the Social Media and Democracy Research Grants from Social Science Research Council (SSRC). Data and tools provided by Facebook.

