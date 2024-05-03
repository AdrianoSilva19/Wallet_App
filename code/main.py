import pandas as pd
from datetime import datetime

def handle_pipeline():
    dataframe = csv_reader()
    holidays_expenses_dict = select_holidays_expenses(dataframe)

def csv_reader():
    reader = pd.read_excel(r"C:\Users\barba\Adri_Work\Wallet_App\data\descarga.xls",skiprows=range(0, 6))
    return reader 


def select_holidays_expenses(general_dataframe):
    general_dataframe['Data Operação'] = pd.to_datetime(general_dataframe['Data Operação'], format='%d-%m-%Y')
    holidays_expenses = {}
    holidays = {"denamrk":["10/04/2024","17/04/2024"],
                "spain":["09/03/2024","15/03/2024"]}
    for country,time_span in holidays.items():
        start_date = datetime.strptime(time_span[0], "%d/%m/%Y")
        end_date = datetime.strptime(time_span[1], "%d/%m/%Y")
        
        expenses = general_dataframe[(general_dataframe['Data Operação'] >= start_date) & (general_dataframe['Data Operação'] <= end_date)]
        
        holidays_expenses[country] = sum(expenses["Montante( EUR )"])

    ## Spain Fix Bokking
    holidays_expenses["spain"] += -466.50

    return holidays_expenses
    



if __name__ == "__main__":
    handle_pipeline()