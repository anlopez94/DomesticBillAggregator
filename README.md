# DomesticBillAggregator

This is a simple application that aggregates domestic bills by month. It is a simple console application that takes an Excel file with a list of different bills and aggregates them by type and month. The application is written in Python and uses the Pandas library for data manipulation.

## Installation
# Clone the repository
git clone https://github.com/anlopez94/DomesticBillAggregator.git

# Navigate to the project directory
cd DomesticBillAggregator

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt

## Usage
The application can be run using the following command:
```bash 
python main.py -filename='example_data' 
```
 The file should be a excel file inside data folder with the following sheets: `internet`, `water`, `gas`, and `electricity`. There is an example of the data typed required in data folder "example_data"
 The application will then aggregate the bills by type and month and save then in results folder. 
