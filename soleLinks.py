import requests
import pandas as pd
import datetime
# Save all data in solelinks.com in a data.txt file
# Convert original data to dataframe and save it as data
# Dataframe ordered by descending release date
url = "http://solelinks.com/api/releases?page=1"
stocks = []

while True:
    res = requests.get(url)
    stocks += res.json()['data']['data']
    print("page %s"%(res.json()['data']['current_page']))
    if not res.json()['data']['next_page_url'] is None:
        url = res.json()['data']['next_page_url']
    else:
        print("Collect All")
        break

with open ("./data.txt", "w+") as f:
        f.write(str(stocks))

df = pd.DataFrame(stocks)
df['release_date'] = pd.to_datetime(df['release_date'])
print(df)
df = df.sort_values(by=['release_date', 'favouriteCount'], ascending=[False, False])
cols = df.columns.tolist()

# Set first column as title
cols[0],cols[1],cols[7], cols[-4] = cols[-4],cols[7], cols[1], cols[0]
df = df[cols].reset_index(drop=True)

df.to_csv("./data.csv", sep='\t', encoding='utf-8')
df.to_pickle("./df")
print("Saved data")
