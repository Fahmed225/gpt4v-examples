import os
import glob
import pandas as pd
import screenshot
import multivision
import image_splitter
import re
import generateConvo
import json
# Read the .csv file
df = pd.read_csv('updated_file.csv')
# df['Items Sold'] = ''
# df['Items Data'] = ''
# df['Generated Convo'] = ''

# # Iterate over the "Website" column
# for index, row in df.iterrows():
#     url = row['Website']
#     # Extract the website name from the URL
#     website_name = re.search('https?://([A-Za-z_0-9.-]+).*', url)
#     if website_name:
#         website_name = website_name.group(1).replace('www.', '')
#     else:
#         website_name = ''
#     output_folder = website_name + "_splits"
#     # # delete screenshot.jpg if it exists
#     # if os.path.exists("screenshot.jpg"):
#     #     os.remove("screenshot.jpg")

#     shot = screenshot.take(url, full_page=True)

#     shots = image_splitter.split(shot, output_folder, 1366, offset=100)

#     print("Extracting supplements sold from " + website_name)
#     response = multivision.look(shots, 'Extract all the supplements sold from these website screenshots and return them in JSON format [{"name":"Item name here"}]. If no supplements are found, return an empty array.')

#     print("Found " + response + " supplements sold on " + website_name)
#     # Store the response in the "Items Sold" column
#     df.at[index, 'Items Sold'] = str(response)

# # Save the DataFrame to a new .csv file
# df.to_csv('updated_file.csv', index=False)

# step 2: extract items in json format from "Items Sold" column
for index, row in df.iterrows():
    itemsSold = row['Items Sold']
    # Extract items from the "Items Sold" column. 
    items = re.search('```json\s*(.*?)\s*```', itemsSold, re.DOTALL)
    if items:
        items = items.group(1)
    else:
        items = ''
    
    print("Generating convo for " + items)
    
    # step 3: generate convo
    # check if items is not empty. 
    if items and items != "[]":
        # convert items to json array
        items = json.loads(items)
        convo = generateConvo.generateConvo(itemsSold)
        print(convo)
        # Store the response in the "Generated Convo" column
        df.at[index, 'Generated Convo'] = convo
    else:
        df.at[index, 'Generated Convo'] = 'No items found'

# Save the DataFrame to a new .csv file
df.to_csv('updated_file.csv', index=False)