import pandas as pd
import ssl
import urllib.request

url = 'https://www.reddit.com/r/nytpips/comments/1u2olce/thursday_june_11_2026_pips_298_thread/.json'
context = ssl._create_unverified_context()
with urllib.request.urlopen(url, context=context) as response:
    data = pd.read_json(response)

print(data.head())

