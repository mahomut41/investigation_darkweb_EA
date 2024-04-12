
# functions.py

import os
import lxml.html


#to take a screenshot
def screenshot_with_element(driver, outputPath, width=None):
        if width==None: 
            width = driver.execute_script('return document.documentElement.scrollWidth')
        
        heightMax = driver.execute_script('return document.documentElement.scrollHeight')
        
        driver.set_window_size(width, heightMax)
        driver.save_screenshot(outputPath)



#to save client code
def save_html(driver, filename):
    client_code = driver.page_source
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(client_code)



#to create directories
def create_or_check_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name, exist_ok=True)


#to parse single html file from a directory
def parse_single_html_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    html = lxml.html.parse(file_path)
    html_root = html.getroot()
    return html_root

#to iterate on html files of the same directory
def process_html_files(directory_name):
    # List all HTML files in the directory
    html_files = [file for file in os.listdir(directory_name) if file.endswith(".html")]

    # Dictionary to store HTML roots for each file
    html_files_data = {}

    # Iterate through each HTML file and extract and insert product data into the corresponding table
    for html_file in html_files:
        # Create the full file path
        file_path = os.path.join(directory_name, html_file)

        # Parse the HTML document using getroot()
        html = lxml.html.parse(file_path)
        html_root = html.getroot()

        # Store the HTML root in the dictionary
        html_files_data[html_file] = html_root

    return html_files_data






