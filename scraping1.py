import requests
from bs4 import BeautifulSoup
question_list = []
answer_list = []
import pandas as pd
# Function to scrape questions and answers from HTML
def scrape_questions_answers(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all question and answer blocks
    qa_blocks = soup.find_all('div', class_='flex flex-wrap text-primaryText h-17')

    # Iterate through each block and extract question and answer
    for block in qa_blocks:
        # Extract the question
        question = block.find('h3', class_='headline2').text.strip()
        
        # Extract the answer
        answer = block.find('p', class_='body1').text.strip()
        question_list.append(question)
        answer_list.append(answer)

# Sample HTML input (can be replaced by fetching live content)
html_content = """"""

# Call the function with the provided HTML content
scrape_questions_answers(html_content)
data_df = pd.DataFrame({
    'Question': question_list,
    'Answer': answer_list
})

# Saving DataFrame to Excel
data_df.to_excel('Science2.xlsx', index=False)
print("Data saved in Excel file successfully!")



import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.answers.com/t/geography?page="
question_list = []
answer_list = []
for page in range(0, 650):
    print("Page No:", page)
    url = base_url + str(page)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Debug: Print the soup object or a portion of it to understand the structure
        # print(soup.prettify())
        
        blocks = soup.find_all('div', class_='qCard')
        
        if not blocks:
            print("No blocks found on this page.")
            continue
        
        for b in blocks:
            question_tag = b.find('p', class_='headline1')
            answer_tag = b.find('div', class_='markdownStyles')
            
            # Debug: Print the tags found
            
            if question_tag:
                question = question_tag.text.strip()
                question_list.append(question)
               
            else:
                question_list.append("No question found")
            
            if answer_tag:
                answer = answer_tag.text.strip()
                answer_list.append(answer)
            else:
                answer_list.append("No answer found")
    
    except requests.RequestException as e:
        print(f"Request failed: {e}")

data_df = pd.DataFrame({
    'Question': question_list,
    'Answer': answer_list
})

data_df.to_excel('Geography.xlsx', index=False)
print("Data saved in Excel file successfully!")


import pandas as pd
import json
import glob

# Path to the directory containing the Excel files
excel_files_path = 'P:\\Sccraping\\*.xlsx'  # Updated for Windows path

# List to hold DataFrames
dfs = []

# Read each Excel file and append DataFrame to the list
for file in glob.glob(excel_files_path):
    print(f"Processing file: {file}")
    df = pd.read_excel(file)
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Convert the combined DataFrame to a list of dictionaries (JSON format)
data = combined_df.to_dict(orient='records')

# Save the JSON data to a file
json_file = 'combined_data.json'
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print("All Excel files successfully converted to a single JSON file!")




import re
import json

def format_latex(text):
    if not isinstance(text, str):
        return text
    
    # Apply LaTeX formatting for common mathematical expressions
    # Simple multiplication and division
    text = re.sub(r'(\d+)\s*x\s*(\d+)', r'$ \text{\1} \times \text{\2} $', text)
    text = re.sub(r'(\d+)\s*\/\s*(\d+)', r'$ \frac{\1}{\2} $', text)
    
    # Ensure the formula format is consistent
    text = re.sub(r'(\bWork\s*=\s*)\d+\s*x\s*\d+', r'\1$ \text{Work} = \text{600} \times \text{45} $', text)
    
    return text

# Load the JSON file
with open('combined_data.json', 'r') as file:
    data = json.load(file)

# Apply LaTeX formatting to each question and answer
for entry in data:
    if 'Question' in entry:
        entry['Question'] = format_latex(entry.get('Question', ''))
    if 'Answer' in entry:
        entry['Answer'] = format_latex(entry.get('Answer', ''))

# Save the updated data to a new JSON file
with open('formatted_data_corrected.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON data with corrected LaTeX formatting has been saved successfully!")


