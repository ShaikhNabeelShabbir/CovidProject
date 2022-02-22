import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.system("cls")


def feb():
    os.system("cls")
    df = pd.read_csv('covid.csv')
    a = list(df.iloc[:29, 0])
    b = list(df.iloc[:29, 1])
    c = list(df.iloc[:29, 2])
    d = list(df.iloc[:29, 3])
    e = list(df.iloc[:29, 4])
    f = list(df.iloc[:29, 5])
    g = list(df.iloc[:29, 6])
    x_index = np.arange(0, 30, 1)
    plt.style.use("fivethirtyeight")
    plt.figure(figsize=(15, 10), dpi=80)
    plt.plot(a, b, marker="o", label="Daily Confirmed")
    plt.plot(a, c, marker="o", label="Total Confirmed")
    plt.plot(a, d, marker="o", label="Daily Recovered")
    plt.plot(a, e, marker="o", label="Total Recovered")
    plt.plot(a, f, marker="o", label="Daily Deceased")
    plt.plot(a, g, marker="o", label="Total Deceased")
    plt.xticks(ticks=x_index)
    plt.title("----COVID-19----")
    plt.xlabel("February")
    plt.ylabel("Number of Cases")
    plt.grid(True, color='k', linestyle=':')
    plt.tight_layout()
    plt.legend()
    plt.show()
    main()


def march():
    os.system("cls")

    df = pd.read_csv('covid.csv')
    a = list(df.iloc[29:60, 0])
    b = list(df.iloc[29:60, 1])
    c = list(df.iloc[29:60, 2])
    d = list(df.iloc[29:60, 3])
    e = list(df.iloc[29:60, 4])
    f = list(df.iloc[29:60, 5])
    g = list(df.iloc[29:60, 6])
    x_index = np.arange(0, 32, 1)
    plt.style.use("fivethirtyeight")
    plt.figure(figsize=(15, 10), dpi=80)
    plt.plot(a, b, marker="o", label="Daily Confirmed")
    plt.plot(a, c, marker="o", label="Total Confirmed")
    plt.plot(a, d, marker="o", label="Daily Recovered")
    plt.plot(a, e, marker="o", label="Total Recovered")
    plt.plot(a, f, marker="o", label="Daily Deceased")
    plt.plot(a, g, marker="o", label="Total Deceased")
    plt.xticks(ticks=x_index)
    plt.title("----COVID-19----")
    plt.xlabel("March")
    plt.ylabel("Number of Cases")
    plt.grid(True, color='k', linestyle=':')
    plt.tight_layout()
    plt.legend()
    plt.show()
    main()


def april():
    os.system("cls")

    df = pd.read_csv('covid.csv')
    a = list(df.iloc[60:90, 0])
    b = list(df.iloc[60:90, 1])
    c = list(df.iloc[60:90, 2])
    d = list(df.iloc[60:90, 3])
    e = list(df.iloc[60:90, 4])
    f = list(df.iloc[60:90, 5])
    g = list(df.iloc[60:90, 6])
    x_index = np.arange(0, 31, 1)
    plt.style.use("fivethirtyeight")
    plt.figure(figsize=(15, 10), dpi=80)
    plt.plot(a, b, marker="o", label="Daily Confirmed")
    plt.plot(a, c, marker="o", label="Total Confirmed")
    plt.plot(a, d, marker="o", label="Daily Recovered")
    plt.plot(a, e, marker="o", label="Total Recovered")
    plt.plot(a, f, marker="o", label="Daily Deceased")
    plt.plot(a, g, marker="o", label="Total Deceased")
    plt.xticks(ticks=x_index)
    plt.title("----COVID-19----")
    plt.xlabel("April")
    plt.ylabel("Number of Cases")
    plt.grid(True, color='k', linestyle=':')
    plt.tight_layout()
    plt.legend()
    plt.show()
    main()
    
    
def may():

       df = pd.read_csv('covid.csv')

       a = list(df.iloc[90:104,0])
       b = list(df.iloc[90:104,1])
       c = list(df.iloc[90:104,2])
       d = list(df.iloc[90:104,3])
       e = list(df.iloc[90:104,4])
       f = list(df.iloc[90:104,5])
       g = list(df.iloc[90:104,6])
       
       x_index = np.arange(0, 34, 1)

       plt.style.use("fivethirtyeight")

       plt.figure(figsize=(15, 10), dpi=80)

       plt.xticks(ticks=x_index)
       plt.plot(a, b, marker="o", label="Daily Confirmed")
       plt.plot(a, c, marker="o", label="Total Confirmed")
       plt.plot(a, d, marker="o", label="Daily Recovered")
       plt.plot(a, e, marker="o", label="Total Recovered")
       plt.plot(a, f, marker="o", label="Daily Deceased")
       plt.plot(a, g, marker="o", label="Total Deceased")
       

       plt.title("----COVID-19----")
       plt.xlabel("May")
       plt.ylabel("Number of Cases")

       plt.grid(True, color='k', linestyle=':')
       plt.tight_layout()
       plt.legend()
       plt.show()
       main()


def main():
    os.system("cls")

    print("Select the month of which you wish to see the covid statistical graph: ")
    choice = int(input('1)FEBRUARY\n2)MARCH\n3)APRIL\n4)MAY\n5)EXIT\n'))
    if choice == 1:
        feb()
    elif choice == 2:
        march()
    elif choice == 3:
        april()
    elif choice == 4:
        may()
    elif choice == 5:
        quit()
    else:
        print("Unknown choice")


main()
