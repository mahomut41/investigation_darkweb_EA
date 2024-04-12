import sqlite3

# Database initialization function
def initialize_database():
    # Connect to SQLite database (create a new file if it doesn't exist)
    connection = sqlite3.connect('evergreen_avenue.db')
    return connection



#create a table in the database to store the category name and umber of results
def create_table_category(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS category_name(
            id INTEGER PRIMARY KEY,
            category TEXT,
            number_of_titles TEXT
            
        )
    ''')
    connection.commit()


#insert into the table category
def insert_category(connection, category, number_of_titles):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO category_name (category, number_of_titles) VALUES (?, ?)', (category, number_of_titles,))
    connection.commit()


#create a table to store the sorting options available
def create_table_sorting_options(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sorting_options(
            id INTEGER PRIMARY KEY,
            sorting_option TEXT
            
        )
    ''')
    connection.commit()


#insert into the table all the sorting options available
def insert_sorting_options(connection, sorting_text):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO sorting_options (sorting_option) VALUES (?)', (sorting_text,))
    connection.commit()



# Create a table in the database to store items based on the sorting option
def create_table_sorting_options_separate(connection, sorting_option_text):
    cursor = connection.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {sorting_option_text} (
            id INTEGER PRIMARY KEY,
            Passport_Type TEXT,
            Price TEXT,
            Link TEXT
        )
    ''')
    connection.commit()

# Insert into each sorting option table its corresponding data
def insert_table_sorting_options_separate(connection, sorting_option_text, item):
    cursor = connection.cursor()
    cursor.execute(f'''
        INSERT INTO {sorting_option_text} (Passport_Type, Price, Link)
        VALUES (?, ?, ?)
    ''', (item['Passport Type'], item['Price'], item['Link']))
    connection.commit()




def create_table_passport_description(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Passport_descriptions (
            id INTEGER PRIMARY KEY,
            PassportTitle TEXT,
            Description TEXT
        )
    ''')
    connection.commit() 


def insert_table_passport_description(connection, passport_title, description):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Passport_descriptions (PassportTitle, Description)
        VALUES (?, ?)
    ''', (passport_title, description))
    connection.commit() 


# Create a table for product details if it doesn't exist
def create_table_passport_type(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Product_types (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Option TEXT,
            Price TEXT
        )
    ''')
    connection.commit()


def insert_table_passport_type(connection, title, dropdown_option_text, price_text):
    cursor = connection.cursor()
    cursor.execute('''
                        INSERT INTO Product_types (Title, Option, Price)
                        VALUES (?, ?, ?)
                    ''', (title, dropdown_option_text, price_text))
    connection.commit()


# Create a table shipping_details
def create_table_shipping_details(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart_totals (
            id INTEGER PRIMARY KEY,
            Subtotal TEXT,
            ShippingInfo TEXT,
            ShippingTo TEXT,
            Total TEXT
        )
    ''')
    connection.commit()


# Insert into the table shipping_details
def insert_table_shipping_details(connection, price, shipping_details, total_subtitle, total_price):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO cart_totals (Subtotal, ShippingInfo, ShippingTo, Total) VALUES (?, ?, ?, ?)',
                   (price, shipping_details, total_subtitle, total_price))
    connection.commit()



# create the billing details table
def create_table_billing_form_details(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Billing_details (
            id INTEGER PRIMARY KEY,
            FieldType TEXT,
            FieldName TEXT,
            Placeholder TEXT,
            IsRequired BOOLEAN
        )
    ''')
    connection.commit()


# insert billing details into the table
def insert_table_billing_form_details(connection, field_type, field_name, placeholder, is_required):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Billing_details (FieldType, FieldName, Placeholder, IsRequired)
        VALUES (?, ?, ?, ?)
    ''', (field_type, field_name, placeholder, is_required))
    connection.commit()


# create shipping country table
def create_table_shipping_country(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Shipping_country (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CountryName TEXT,
            Shipping TEXT
        )
    ''')
    connection.commit()

# insert shipping country into the table
def insert_table_shipping_country(connection, option_text, free_shipping_label):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Shipping_country (CountryName, Shipping)
        VALUES (?, ?)
    ''', (option_text, free_shipping_label))
    connection.commit()
    

def create_table_payment_info(connection):
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payment_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                summary TEXT,
                crypto_amount TEXT,
                address TEXT
            )
        ''')
        connection.commit()



# Function to insert values into the payment_info table
def insert_table_payment_info(connection, payment_info):
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO payment_info (summary, crypto_amount, address)
            VALUES (?, ?, ?)
        ''', (
            payment_info['Summary'],
            payment_info['CryptoAmount'],
            payment_info['Address']
        ))
        connection.commit()







