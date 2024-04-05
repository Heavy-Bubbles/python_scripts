import pandas as pd
import shutil, os

scraper = pd.read_html('https://en.wikipedia.org/wiki/List_of_sovereign_states')

# check table index

# for idx, table in enumerate(scraper):
#     print("************************************")
#     print(idx)
#     print(table)

list_of_sovereign_states = scraper[1]

# panda dataframe
df = pd.DataFrame(list_of_sovereign_states)
print(df)

file_name = "ListOfSovereignStates.csv"

directory = os.getcwd()
file_path = os.path.join(directory, file_name)

if os.path.exists(file_path):
    os.remove(file_path)

new_file = df.to_csv(file_name)
