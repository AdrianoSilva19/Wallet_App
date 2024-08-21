import seaborn as ses
import matplotlib.pyplot as plt
import numpy as np

class Viewer:

    def __init__(self, whole_data):
        self.whole_data = whole_data

    def barplot_monthly_balance(self):
        """Bar plot generator for the wages and holidays expenses"""
        wages = self.whole_data.get("ctw_wages", {})
        holidays = self.whole_data.get("holiday_expenses", {})
        house_expenses = self.whole_data.get("house_expenses", {})
        
        # Combine keys (months) from both dictionaries and sort them
        months = sorted(wages.keys() | holidays.keys()| house_expenses.keys())
        
        # Create lists of values for wages and holidays
        wage_values = [wages.get(month, 0) for month in months]
        holiday_values = [holidays.get(month, 0) for month in months]
        house_values = [house_expenses.get(month, 0) for month in months]

        # Set up the bar width and x positions
        bar_width = 0.70
        x = np.arange(len(months))

        # Create the bar plots
        plt.bar(x , wage_values, width=bar_width, label='Wages', color='green')
        plt.bar(x , holiday_values, width=bar_width, label='Holidays Expenses', color='red')
        plt.bar(x , house_values, width=bar_width, label='House Expenses', color='pink')

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
        wages = self.whole_data.get("ctw_wages", {})
        holidays = self.whole_data.get("holiday_expenses", {})
        house_expenses = self.whole_data.get("house_expenses", {})
        
        # Combine keys (months) from both dictionaries and sort them
        months = sorted(wages.keys() | holidays.keys()| house_expenses.keys())

         # Calculate the balance for each month
        balances = [wages.get(month, 0) + holidays.get(month, 0) + house_expenses.get(month, 0) for month in months]

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


