import pandas as pd
import matplotlib.pyplot as plt

#Read file into data frame and printing data frame
df=pd.read_csv('country_wise_latest.csv')
print(df)

#Function for plotting Line plot
def lineplot():   
    plt.figure() #Plotting Countries with labels
    plt.plot(df["Country"],df["Deaths"],label="Deaths")
    plt.plot(df["Country"],df["Recovered"],label="Recovered")
    plt.xticks(rotation=90)
    plt.xlabel("Country") #Setting labels and showing the legend
    plt.ylabel("Cases")
    plt.legend()
    plt.title("COVID-19 cases")
    plt.show()
lineplot() #Calling defined function for line graph

#Function for bar graph
def barplot():
    plt.figure()  #plotting countries with label
    plt.bar(df["Country"],df["Deaths"],label="Deaths", alpha=0.4, color="green")
    plt.bar(df["Country"],df["Recovered"],label="Recovered", alpha=0.4, color="blue")
    plt.xticks(rotation=90)
    plt.xlabel("Country")  #setting labels and showing the legend
    plt.ylabel("Cases")
    plt.legend()
    plt.title("COVID-19 cases")
    plt.legend()
    plt.show()
barplot()  #Calling defined function for bar graph

#Function for plotting Pie Chart
def pieplot():
    plt.figure() #plotting confrimed cases of the countries
    plt.pie(df["Confirmed"],autopct='%1.1f%%')
    plt.legend(bbox_to_anchor = (1.0,1.0),labels=df["Country"])
    plt.title("Covid-19 Cases",size=19)
    plt.show()
pieplot()  #calling defined function for pie chart
