import pandas as pd
from datetime import datetime

class Transformer:
    def __init__(self, dataframe:pd.DataFrame):
        self.dataframe = dataframe

    def select_holidays_expenses(self):
        columns = ['Data Operação', 'Montante( EUR )']
        self.dataframe[columns[0]] = pd.to_datetime(self.dataframe[columns[0]], format='%d-%m-%Y')
        holidays_expenses = {}
        holidays = {"denamark":["10/04/2024","17/04/2024"],
                    "spain":["09/03/2024","15/03/2024"]}
        for country,time_span in holidays.items():
            start_date = datetime.strptime(time_span[0], "%d/%m/%Y")
            end_date = datetime.strptime(time_span[1], "%d/%m/%Y")
            
            expenses = self.dataframe[(self.dataframe[columns[0]] >= start_date) & (self.dataframe[columns[0]] <= end_date)]
            
            holidays_expenses[country] = sum(expenses[columns[1]])

        ## Spain Fix Bokking
        holidays_expenses["spain"] += -466.50

        return holidays_expenses
    
    def extract_wages(self):
        wages_dict = {}
        columns = ['Descrição', 'Montante( EUR )']
        wages = self.dataframe[self.dataframe[columns[0]].str.contains("Ordenado de")]
        wages_dict["Ordenado de Critical Techworks, S.a."] = wages[columns[1]].sum()
        return wages_dict
