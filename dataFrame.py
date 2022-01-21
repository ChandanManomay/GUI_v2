import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

# from pandas.core.frame import DataFrame
# from pandastable import Table

# root = tk.Tk()

# frame = tk.Frame(root)
# frame.pack()
# df = pd.read_csv("DashboardView.csv")
# pt = Table(frame, dataframe=df)
# pt.columncolors["STATUS"] = "red"  # color a specific column
# pt.redraw()
# pt.show()
df = pd.read_csv(
    r"C:\Users\kapur\OneDrive\Documents\GitHub\CustomerServiceApp\GUI_v2\DashboardView.csv"
)
plotdata = df.iloc[:, 3:5]
# print(plotdata)
plotdata.plot(kind="pie", subplots=True, labels=df["Extraction Template"])
plt.show()

# root.mainloop()

