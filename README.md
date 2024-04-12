## Project Name

- **Internet Investigation on the Sale of Passports on the Dark Web**

A Python script for scraping passport-related product information from a dark web e-commerce website. The script utilizes Selenium for web scraping, SQLite for database interaction, and custom functions for various tasks.

## Operating System Information

- **Operating System:** Apple Virtual Machine 1
- **Chip:** Apple M1 Pro (Virtual)

### Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Web Scraping Methods](#web-scraping-methods)
6. [Database Structure](#database-structure)

## Overview

This project consists of a Python script designed to scrape passport-related product information from a dark web e-commerce website. It covers functionalities such as navigating the website, capturing HTML content, parsing and extracting data, and storing the information in an SQLite database.

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- **Tor Browser:**
   - Tor must be opened before running the script.
   - [Download Tor Browser](https://www.torproject.org/download/)

- **Firefox Driver:**
- Download the appropriate Firefox Driver (geckodriver) for your system.
        - [Firefox Driver Downloads](https://github.com/mozilla/geckodriver/releases)
   - Place the downloaded geckodriver executable in a specific directory or add it to the system's PATH variable.
   - Instructions for setting up geckodriver for this project can be found in the [official documentation](https://github.com/mozilla/geckodriver).

- **Database Browser for SQLite :**
   - Ensure Database Browser for SQLite is installed on your system.
   - [Database Browser for SQLite Download](https://sqlitebrowser.org/dl/)

## Usage

1. Open Tor Browser and ensure it is running.
2. Run the script before 1 pm and after 10 pm for optimal performance according to UTC+1!

## Web Scraping Methods

This project uses various web scraping methods to select and interact with HTML elements:

1. **cssselect:**
   - Utilizes the `cssselect` library for CSS selector-based element identification.
   - Example: `element = html_root.cssselect('.class-name')`

2. **XPath:**
   - Utilizes the built-in XPath support in the `lxml` library for XPath-based element identification.
   - Example: `element = html_root.xpath('//div[@id="example"]')`

3. **"Get Element" Methods:**
   - Employs Selenium's `find_element` method for locating HTML elements.
   - Example: `element = driver.find_element(By.XPATH, '//div[@class="example"]')`
   - Also uses `WebDriverWait` for dynamic waiting to ensure element visibility before interaction.
   - Example: 
     ```python
     element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, 'example'))
     )
     ```

## Database Structure

The script interacts with an SQLite database, creating and populating tables for various information. Here's an overview of the database structure:

1. **`category_name` Table:**
   - Stores category names and the corresponding number of titles.

2. **`sorting_options` Table:**
   - Holds various sorting options available on the website.

3. **`sorting_options_separate` Tables:**
   - Dynamically created tables for each sorting option, storing passport details.

4. **`Passport_descriptions` Table:**
   - Contains passport titles and descriptions.

5. **`Product_types` Table:**
   - Stores product titles, selected options, and prices.

6. **`cart_totals` Table:**
   - Captures subtotal, shipping info, destination, and total amount.

7. **`Billing_details` Table:**
   - Records billing form field details.

8. **`Shipping_country` Table:**
   - Saves shipping information for different countries.

9. **`payment_info` Table:**
   - Stores payment summary, crypto amount, and address.

Each table serves a specific purpose in organizing and storing data related to passport products, sorting options, billing details, and payment information.# investigation_darkweb_EA
