
import xml.etree.ElementTree as ET
import pandas as pd
import re

tree = ET.parse('C:\\Users\\Admin\\Downloads\\press_import.xml')
root = tree.getroot()

list_values = []
df_cols = ["ID", "Title", "Description"]

for child in root.findall('field_collection_item'):
        ID = child.find('ID').text
        Title = child.find('Title').text
        Description = child.find('Description').text
        Description = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', Description)
        
        list_values.append({"ID": ID, "Title": Title, "Description": Description})
        
# print(list_values)


out_df = pd.DataFrame(list_values, columns = df_cols)

# print(out_df)

out_df.to_excel(r'press.xlsx', index = False)