from bs4 import BeautifulSoup
import json

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the script tag containing the jsonData
script_tag = soup.find('script')
json_data_string = script_tag.contents[0]

# Load JSON data
json_data = json.loads(json_data_string)

# Modify the jsonData
# For example, add a new item to the array
new_item = {"name": "New Item"}
json_data.append(new_item)

# Update the script tag contents with the modified jsonData
script_tag.contents[0] = 'const jsonData = ' + json.dumps(json_data, indent=4) + ';'

# Save the modified HTML content back to the file
with open('index_modified.html', 'w', encoding='utf-8') as modified_file:
    modified_file.write(str(soup))
