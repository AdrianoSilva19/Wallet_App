import seaborn as ses
import matplotlib.pyplot as plt

class Viewer:

    def __init__(self, whole_data):
        self.whole_data = whole_data

    def piechart_wages_holidays(self):
        """Pie chart generator for the holidays expenses
        """
        wages = self.whole_data["wages"]
        holidays = self.whole_data["holidays_expenses"]
        print(wages,holidays)
        keys = wages.keys() | holidays.keys()
        values = [wages.get(k) | holidays.get(k) for k in keys]
        print(keys,values)
        colors = ["red" if i < 0 else "green" for i in values]
       
        plt.pie(values, labels=keys, autopct='%.0f%%', colors=colors)
        plt.show()
  


