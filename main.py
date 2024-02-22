

import argparse
from scripts.agregate_bills import AgregateBills

if __name__ == '__main__':

    # Create the parser and add arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-filename', help="name of file", default='example_data')
    file_name = parser.parse_args().filename
    agregate_facturas = AgregateBills(file_name=file_name)
    agregate_facturas.compute()
    agregate_facturas.save_data()
    print('angela')