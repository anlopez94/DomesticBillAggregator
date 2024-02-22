# DomesticBillAggregator

This is a simple application that aggregates domestic bills. It is a simple console application that takes in a list of bills and aggregates them by type and date. The application is written in Python and uses the pandas library for data manipulation.

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
 The file should be a excel file inside data folder with the following sheets: `internet`, `water`, `gas`, and `electricity`. The application will then aggregate the bills by type and date and save then in results folder. There is an example of the data typed required in data folder "example_data"
