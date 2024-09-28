# Product Scraper for Moustapha Labban Website

## Description

This Python script scrapes product information from the Moustapha Labban website (https://moustaphalabban.com). It collects detailed product data from all pages of the "all collections" section and saves it to a CSV file.

## Setup and Installation

### 1. Install Python

1. Visit the official Python website: https://www.python.org/downloads/
2. Download the latest version of Python for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the installation wizard.
   - On Windows, make sure to check the box that says "Add Python to PATH" during installation.
4. To verify the installation, open a command prompt or terminal and type:
   ```
   python --version
   ```
   This should display the installed Python version.

### 2. Install PyCharm (IDE)

1. Go to the PyCharm download page: https://www.jetbrains.com/pycharm/download/
2. Choose between Community (free) or Professional (paid) edition.
3. Download the appropriate version for your operating system.
4. Run the installer and follow the installation wizard.
5. Launch PyCharm after installation.

### 3. Set Up the Project

1. Open PyCharm.
2. Click on "Create New Project".
3. Choose a location for your project and give it a name (e.g., "product_scraper").
4. Select the previously installed Python interpreter.
5. Click "Create" to set up the project.

### 4. Install Required Libraries

1. In PyCharm, open the Terminal (usually at the bottom of the window).
2. Install the required libraries by typing:
   ```
   pip install requests beautifulsoup4 lxml
   ```

### 5. Create the Script

1. In PyCharm, right-click on your project folder in the left sidebar.
2. Select New > Python File.
3. Name the file `main.py`.
4. Copy and paste the provided script into this file.

## Usage

1. In PyCharm, right-click on `main.py` in the project explorer.
2. Select "Run 'main'".
3. The script will start running, and you'll see progress updates in the console at the bottom of PyCharm.
4. Once completed, a CSV file named `detailed_info_product_DD_MM_YYYY.csv` (where DD_MM_YYYY is the current date) will be created in your project folder.

## Features

- Scrapes product information from multiple pages
- Extracts detailed product data including ID, name, barcode, SKU, attributes, descriptions, categories, prices, and image URLs
- Saves data to a CSV file with a timestamp in the filename
- Provides progress updates during execution

## Output

The script generates a CSV file with the following columns:

- Product_ID
- Product_Name
- Product_Barcode
- Product_Sku
- Product_Attribute_color
- Product_Attribute_size
- Product_Descriptions
- Product_Categorise
- Product_Price
- Product_Sale_price
- Product_Image

## Notes

- The script is set to scrape 64 pages by default. Adjust the range in the `for` loop if needed.
- Be mindful of the website's robots.txt file and terms of service when using this scraper.
- Consider adding delays between requests to avoid overloading the server.

## Troubleshooting

If you encounter any issues:
1. Ensure all libraries are correctly installed.
2. Check your internet connection.
3. Verify that the website structure hasn't changed, which could break the scraper.

## Disclaimer

This script is for educational purposes only. Ensure you have permission to scrape the website and comply with all applicable laws and website terms of service.