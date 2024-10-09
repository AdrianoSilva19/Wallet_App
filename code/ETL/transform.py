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
        fuel_expenses = self.extract_fuel_expenses(self.dataframe)
        beverages_and_food = self.extract_beverages_and_food(self.dataframe)
        self.month_balance = {k: {**ctw_wages[k], **fuel_expenses[k], **house_expenses[k],**beverages_and_food[k], **holiday_expenses.get(k, {})} for k in ctw_wages.keys() 
                              | fuel_expenses.keys() | house_expenses.keys() | beverages_and_food.keys() | holiday_expenses.keys()}
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
        holidays_expenses = {2024: {"holidays":{}}}
        holidays = {"denamark":["10/04/2024","17/04/2024"],
                    "spain":["09/03/2024","15/03/2024"]}
        for country,time_span in holidays.items():
            start_date = datetime.strptime(time_span[0], "%d/%m/%Y")
            end_date = datetime.strptime(time_span[1], "%d/%m/%Y")
            
            expenses = dataframe[(dataframe[columns[0]] >= start_date) & (dataframe[columns[0]] <= end_date)]
            
            holidays_expenses[2024]["holidays"][start_date.strftime("%B")] = sum(expenses[columns[1]])
        
        airbnb_geres = dataframe[dataframe["Descrição"].str.contains("Airbnb")]
        holidays_expenses[2024]["holidays"]["June"] = sum(airbnb_geres[columns[1]])

        ## Spain Fix Bokking
        holidays_expenses[2024]["holidays"][start_date.strftime("%B")] += -466.50
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
        wages_year_month = wages.groupby([wages['Date'].dt.year.rename('year'), 
                   wages['Date'].dt.month_name().rename('month')])['Montante( EUR )'].sum().reset_index()
        wages_year_month.set_index(['year', 'month'], inplace=True)
        wages_year_month.rename({columns[1]: 'wages'}, axis=1, inplace=True)
        wages_dict = {year: wages_year_month.loc[year].to_dict() for year in wages_year_month.index.get_level_values(0).unique()}
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
        house_expenses_year_month = house_expenses.groupby([house_expenses['Date'].dt.year.rename('year'), 
                   house_expenses['Date'].dt.month_name().rename('month')])['Montante( EUR )'].sum().reset_index()
        house_expenses_year_month.set_index(['year', 'month'], inplace=True)
        house_expenses_year_month.rename({columns[1]: 'house_expenses'}, axis=1, inplace=True)
        house_expenses_dict = {year: house_expenses_year_month.loc[year].to_dict() for year in house_expenses_year_month.index.get_level_values(0).unique()}
        return house_expenses_dict

    @staticmethod
    def extract_fuel_expenses(dataframe:pd.DataFrame=None,pattern_to_search:str=None)->dict:
        """Method that extracts the fuel expenses from the dataframe and returns a dictionary with the sum of the fuel expenses by month.

        Returns:
            dict: dictionary with the sum of the fuel expenses by month
        """
        columns = ['Descrição', 'Montante( EUR )']
        fuel_expenses = dataframe[dataframe[columns[0]].str.contains("Bp Ponte|E Leclerc|Inter Vila Do Prado", na=False)]
        fuel_expenses_year_month = fuel_expenses.groupby([fuel_expenses['Date'].dt.year.rename('year'), 
                   fuel_expenses['Date'].dt.month_name().rename('month')])['Montante( EUR )'].sum().reset_index()
        fuel_expenses_year_month.set_index(['year', 'month'], inplace=True)
        fuel_expenses_year_month.rename({columns[1]: 'fuel_expenses'}, axis=1, inplace=True)
        fuel_expenses_dict = {year: fuel_expenses_year_month.loc[year].to_dict() for year in fuel_expenses_year_month.index.get_level_values(0).unique()}
        return fuel_expenses_dict
    
    @staticmethod
    def extract_beverages_and_food(dataframe:pd.DataFrame=None,pattern_to_search:str=None)->dict:
        """Method that extracts the beverages and food expenses from the dataframe and returns a dictionary with the sum of the expenses by month.

        Returns:
            dict: dictionary with the sum of the expenses by month
        """
        columns = ['Descrição', 'Montante( EUR )']
        beverages_and_food = dataframe[dataframe[columns[0]].str.contains("Gertal|Pingo Doce|Vending|Mikado|Cervejaria|Pelle|Ramen|Continente|Cozinha", na=False)]
        beverages_and_food_year_month = beverages_and_food.groupby([beverages_and_food['Date'].dt.year.rename('year'), 
                   beverages_and_food['Date'].dt.month_name().rename('month')])['Montante( EUR )'].sum().reset_index()
        beverages_and_food_year_month.set_index(['year', 'month'], inplace=True)
        beverages_and_food_year_month.rename({columns[1]: 'beverages_and_food'}, axis=1, inplace=True)
        beverages_and_food_dict = {year: beverages_and_food_year_month.loc[year].to_dict() for year in beverages_and_food_year_month.index.get_level_values(0).unique()}
        return beverages_and_food_dict