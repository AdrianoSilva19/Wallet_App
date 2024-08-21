import pandas as pd
from datetime import datetime

class Transformer:
    def __init__(self, dataframe:pd.DataFrame):
        self.dataframe = dataframe
        self.month_balance = {}



    def handler(self):
        holiday_expenses = self.select_holidays_expenses(self.dataframe)
        ctw_wages = self.extract_wages(self.dataframe)
        house_expenses = self.extract_house_expenses(self.dataframe)
        self.month_balance["ctw_wages"] = ctw_wages
        self.month_balance["holiday_expenses"] = holiday_expenses
        self.month_balance["house_expenses"] = house_expenses
        return self.month_balance
    
    @staticmethod
    def select_holidays_expenses(dataframe=None):

        columns = ['Data Operação', 'Montante( EUR )']
        dataframe[columns[0]] = pd.to_datetime(dataframe[columns[0]], format='%d-%m-%Y')
        holidays_expenses = {}
        holidays = {"denamark":["10/04/2024","17/04/2024"],
                    "spain":["09/03/2024","15/03/2024"]}
        for country,time_span in holidays.items():
            start_date = datetime.strptime(time_span[0], "%d/%m/%Y")
            end_date = datetime.strptime(time_span[1], "%d/%m/%Y")
            
            expenses = dataframe[(dataframe[columns[0]] >= start_date) & (dataframe[columns[0]] <= end_date)]
            
            holidays_expenses[start_date.strftime("%B")] = sum(expenses[columns[1]])
        
        airbnb_geres = dataframe[dataframe["Descrição"].str.contains("Airbnb")]
        holidays_expenses["June"] = sum(airbnb_geres[columns[1]])

        ## Spain Fix Bokking
        holidays_expenses[start_date.strftime("%B")] += -466.50
        return holidays_expenses
    
    @staticmethod
    def extract_wages(dataframe=None):
        # Convert the dataframe's date column to datetime format
        dataframe['Date'] = pd.to_datetime(dataframe['Data valor'], format="%d-%m-%Y")

        columns = ['Descrição', 'Montante( EUR )']
        wages = dataframe[dataframe[columns[0]].str.contains("Ordenado de")]
        wages_by_month = wages.groupby(wages['Date'].dt.strftime('%B'))[columns[1]].sum()
        wages_dict = wages_by_month.to_dict()
        return wages_dict
    
    @staticmethod
    def extract_house_expenses(dataframe=None):
        columns = ['Descrição', 'Montante( EUR )']
        house_expenses = dataframe[dataframe[columns[0]].str.contains("Renda|Americo", na=False)]
        house_expenses_by_month = house_expenses.groupby(house_expenses['Date'].dt.strftime('%B'))[columns[1]].sum()
        house_expenses_dict = house_expenses_by_month.to_dict()
        return house_expenses_dict

