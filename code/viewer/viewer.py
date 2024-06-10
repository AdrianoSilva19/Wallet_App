import seaborn as ses
import matplotlib.pyplot as plt

class Viewer:

    def __init__(self, whole_data):
        self.whole_data = whole_data

    def piechart_holidays(self):

        holidays = self.whole_data["holidays_expenses"]
        keys = holidays.keys()
        values = [ holidays.get(k) for k in keys]
        colors = ["red" if i < 0 else "green" for i in values]
       
        plt.pie(values, labels=keys, autopct='%.0f%%', colors=colors)
        plt.show()
  


