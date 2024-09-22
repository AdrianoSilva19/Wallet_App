import pandas as pd
from datetime import datetime
try:
    from generic_utils._utils import logging_decorator_factory
except ImportError:
    from code.generic_utils._utils import logging_decorator_factory
class Transformer:
    """This class is responsible for transforming the data extracted from the raw dataframe
    """
    def __init__(self, dataframe:pd.DataFrame):
        """Constructor for the Transformer class

        Args:
            dataframe (pd.DataFrame): raw dataframe extracted from the excel file
        """
        self.dataframe = dataframe
        self.month_balance = {}



    def handler(self)->dict:
        """This method is responsible for calling the methods that will transform the data

        Returns:
            dict: final dictionary with the transformed data, separated by categories into multiple nested dictionaries
        """
        holiday_expenses = self.select_holidays_expenses(self.dataframe)
        ctw_wages = self.extract_wages(self.dataframe)
        house_expenses = self.extract_house_expenses(self.dataframe)
        self.month_balance["ctw_wages"] = ctw_wages
        self.month_balance["holiday_expenses"] = holiday_expenses
        self.month_balance["house_expenses"] = house_expenses
        return self.month_balance
    
    @staticmethod
    def select_holidays_expenses(dataframe:pd.DataFrame=None, holidays_start_end_dates:dict=None)->dict:
        """Method that selects all the expenses related to holidays and returns a dictionary with the sum of the expenses by month. 
        To this a given set of holidays is considered, with a start and end date, and the expenses are summed between these dates.

        Args:
            dataframe (pd.DataFrame, optional): Original Dataframe were holidays expenses will be extracted. Defaults to None.

        Returns:
            dict: dictionary with the sum of the expenses by month
        """
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
    def extract_wages(dataframe:pd.DataFrame=None,pattern_to_search:str=None)->dict:
        """Method that extracts the wages from the dataframe and returns a dictionary with the sum of the wages by month.
        The entity that provides the wages is passed as a pattern_to_search to filter the wages.

        Args:
            dataframe (_type_, optional): original dataframe where wages will be extracted. Defaults to None.

        Returns:
            dict: dictionary with the sum of the wages by month
        """
        # Convert the dataframe's date column to datetime format
        dataframe['Date'] = pd.to_datetime(dataframe['Data valor'], format="%d-%m-%Y")

        columns = ['Descrição', 'Montante( EUR )']
        wages = dataframe[dataframe[columns[0]].str.contains("Ordenado de")]
        wages_by_month = wages.groupby(wages['Date'].dt.strftime('%B'))[columns[1]].sum()
        wages_dict = wages_by_month.to_dict()
        return wages_dict
    
    @staticmethod
    def extract_house_expenses(dataframe:pd.DataFrame=None,pattern_to_search:str=None)->dict:
        """Method that extracts the house expenses from the dataframe and returns a dictionary with the sum of the house expenses by month.
        Housing expenses are considered to be the rent and the expenses related to the house such as electricity and watter.
        To this end the pattern_to_search is used to filter the expenses related to the house.

        Args:
            dataframe (pd.DataFrame, optional): original dataframe where housing costs will be extracted. Defaults to None.
            pattern_to_search (str, optional): Pattern to be seached for housing expenses. Defaults to None.

        Returns:
            dict: _description_
        """
        columns = ['Descrição', 'Montante( EUR )']
        house_expenses = dataframe[dataframe[columns[0]].str.contains("Renda|Americo", na=False)]
        house_expenses_by_month = house_expenses.groupby(house_expenses['Date'].dt.strftime('%B'))[columns[1]].sum()
        house_expenses_dict = house_expenses_by_month.to_dict()
        return house_expenses_dict

