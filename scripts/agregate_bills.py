
import pandas as pd
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

class AgregateBills:
    def __init__(self, file_name):
        self.facturas = ['gas', 'electricity', 'water', 'internet']
        self.file = file_name
        self.data_path = "data/"
        self.result_path = "results/"

    def compute(self):
        self._load_data()
        self._process_data()

    def save_data(self):
        self.data_processed.to_excel(self.result_path + self.file + "_processed.xlsx", sheet_name='general')

    def _process_data(self):
        self.gas_processed = pd.DataFrame.from_dict(self._process_df(self.gas), orient='index',columns=['gas'])
        self.electricity_processed = pd.DataFrame.from_dict(self._process_df(self.electricity), orient='index',columns=['electricity'])
        self.water_processed = pd.DataFrame.from_dict(self._process_df(self.water), orient='index',columns=['water'])
        self.internet_processed = pd.DataFrame.from_dict(self._process_df(self.internet), orient='index',columns=['internet'])
        #cocatenate all the dataframes
        self.data_processed = pd.concat([self.gas_processed, self.electricity_processed, self.water_processed, self.internet_processed], axis=1, sort=False)
        #sum all columns in a new column called total
        self.data_processed['total'] = self.data_processed.sum(axis=1)

    def _add_value_to_dic(self, dic, key, value):
        if key in dic.keys():
            dic[key] = dic[key] + value
        else:
            dic[key] = value
        return dic

    def _process_df(self, df):
        imports_per_month = {}
        df['days'] = (df['fin'] - df['init']).dt.days
        df['import_day'] = df['import'] / df['days']

        for index, row in df.iterrows():
            first_month = datetime(row['init'].year, row['init'].month, 1)
            last_month = datetime(row['fin'].year, row['fin'].month, 1)
            month = first_month
            while month <= last_month:

                if month == first_month and month == last_month:
                    #number of days lef in the month
                    days = row['fin'].day - row['init'].day

                elif month == first_month:
                    #number of days lef in the month
                    days = row['init'].to_period('M').end_time.day - row['init'].day

                elif month == last_month:
                    #number fo days in this month until that moment
                    days = row['fin'].day
                else:
                    #number of days in the month
                    days = row['fin'].to_period('M').end_time.day

                self._add_value_to_dic(imports_per_month, month, row['import_day'] * days)
                month = month + relativedelta(months=1)


        return imports_per_month


    def _load_data(self):

        for factura in self.facturas:
            locals()[factura] = pd.read_excel(self.data_path + self.file + '.xlsx', sheet_name=factura)

            fechas = ['init', 'fin', 'emitida', 'charged']
            for fecha in fechas:
                ts_formats = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d', '%d-%m-%y', '%y-%m-%d', '%d/%m/%y', '%y/%m/%d',
                              '%d-%m-%Y H:M:S', '%Y-%m-%d H:M:S', '%d/%m/%Y H:M:S', '%Y/%m/%d H:M:S', '%d-%m-%y H:M:S',
                              '%y-%m-%d H:M:S', '%d/%m/%y H:M:S', '%y/%m/%d H:M:S']
                for format in ts_formats:
                    locals()[factura][fecha] = pd.to_datetime(locals()[factura][fecha], format=format)
                    locals()[factura][fecha] = locals()[factura][fecha].dt.strftime('%Y-%m-%d')
                    locals()[factura][fecha] = pd.to_datetime(locals()[factura][fecha], format='%Y-%m-%d')

        self.gas = locals()['gas']
        self.electricity = locals()['electricity']
        self.water = locals()['water']
        self.internet = locals()['internet']