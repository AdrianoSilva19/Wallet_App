import seaborn as ses
import matplotlib.pyplot as plt
import numpy as np

class Viewer:

    def __init__(self, whole_data):
        self.whole_data = whole_data
        self.holidays = self.whole_data.get("holiday_expenses", {})
        self.wages = self.whole_data.get("ctw_wages", {})
        self.house_expenses = self.whole_data.get("house_expenses", {})
        self.fuel_expenses = self.whole_data.get("fuel_expenses", {})
        self.beverages_and_food = self.whole_data.get("beverages_and_food", {})

    def barplot_monthly_balance(self):
        """Bar plot generator for the wages and holidays expenses"""
        
        # Combine keys (months) from both dictionaries and sort them
        months = sorted(self.wages.keys() | self.holidays.keys()| self.house_expenses.keys() | self.fuel_expenses.keys() | self.beverages_and_food.keys())
        
        # Create lists of values for wages and holidays
        wage_values = [self.wages.get(month, 0) for month in months]
        holiday_values = [self.holidays.get(month, 0) for month in months]
        house_values = [self.house_expenses.get(month, 0) for month in months]
        fuel_values = [self.fuel_expenses.get(month, 0) for month in months]
        beverages_values = [self.beverages_and_food.get(month, 0) for month in months]

        # Set up the bar width and x positions
        bar_width = 0.70
        x = np.arange(len(months))

        # Create the bar plots
        plt.bar(x , wage_values, width=bar_width, label='Wages', color='green')
        plt.bar(x , holiday_values, width=bar_width, label='Holidays Expenses', color='red')
        plt.bar(x , house_values, width=bar_width, label='House Expenses', color='pink')
        plt.bar(x , fuel_values, width=bar_width, label='Fuel Expenses', color='lightcoral')
        plt.bar(x , beverages_values, width=bar_width, label='Beverages and Food', color='maroon')

        # Add labels and title
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.title('Monthly balance')
        plt.xticks(ticks=x, labels=months, rotation=45)
        plt.axhline(0, color='black',linewidth=0.5)

        # Add a legend
        plt.legend()

        # Show the plot
        plt.tight_layout()
        plt.show()
    
    def barplot_general(self):
        
        # Combine keys (months) from both dictionaries and sort them
        months = sorted(self.wages.keys() | self.holidays.keys()| self.house_expenses.keys() | self.fuel_expenses.keys()| self.beverages_and_food.keys())

         # Calculate the balance for each month
        balances = [self.wages.get(month, 0) + self.holidays.get(month, 0) + self.house_expenses.get(month, 0) + self.fuel_expenses.get(month,0) + self.beverages_and_food.get(month,0) for month in months]

        # Set the colors based on whether the balance is positive or negative
        colors = ['green' if balance >= 0 else 'red' for balance in balances]

        # Set up the bar width and x positions
        x = np.arange(len(months))

        # Create the bar plot
        plt.bar(x, balances, color=colors)

        # Add labels and title
        plt.xlabel('Month')
        plt.ylabel('Balance')
        plt.title('Monthly Balance')
        plt.xticks(ticks=x, labels=months, rotation=45)
        plt.axhline(0, color='black', linewidth=0.5)  # Line at y=0 to separate positive and negative

        # Show the plot
        plt.tight_layout()

        plt.show()


