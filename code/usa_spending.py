import os

import bs4
import pandas as pd
import requests


def get_api_endpoints() -> pd.DataFrame:
    url = "https://api.usaspending.gov/docs/endpoints"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text)
    endpoint_str = str(soup.find("table"))
    endpoint_df = pd.read_html(endpoint_str)
    endpoint_df = endpoint_df[0].copy()
    return endpoint_df


def make_api_call(endpoint: str) -> requests.models.Response:
    base_url = "https://api.usaspending.gov"
    api_call = f"{base_url}{endpoint}"
    res = requests.get(api_call)
    return res
