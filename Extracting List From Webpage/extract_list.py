import pandas as pd

scraper = pd.read_html('https://en.wikipedia.org/wiki/List_of_sovereign_states')

# check table index

# for idx, table in enumerate(scraper):
#     print("************************************")
#     print(idx)
#     print(table)

scraper[1].to_csv("ListOfSovereignStates.csv")