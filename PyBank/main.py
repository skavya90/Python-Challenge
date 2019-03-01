# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:37:27 2019

@author: skavy
"""
import csv
import os

datapath = os.path.join('C:\\','users','skavy','Desktop','PythonStuff','budget_data.csv')

months = []
amount = []
change = []
G_Increase = 0
G_Decrease = 0
with open(datapath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Checks the list of rows in csvfile and remove duplicates
    budget = list(csv.reader(csvfile, delimiter=','))
    new_budget = [a for i, a in enumerate(budget) if a not in budget[:i]] 
    for row in new_budget:
        #Updates months list with new months
        months.append(row[0]) 
        
        #Updates amount list with new values
        amount.append(int(row[1]))
        
        #Calculating average of profit/losses
    for k in range(len(amount) -1):
        change.append((amount[k+1])-(amount[k]))
        diff = (amount[k+1] - amount[k])
        if (diff > G_Increase):
            G_Increase = diff
            G_Increase_Month = months[k+1]
        if (diff < G_Decrease):
            G_Decrease = diff
            G_Decrease_Month = months[k+1] 
    #Gets the average change by dividing total of changes by number of changes  
    average_change = round((sum(change) / len(change)), 2)
    #Gets count for number of months in total        
    print(f"Total Months: {len(months)}")
    print(f"Total: {(sum(amount))}")
    print(f"Average Change: {(average_change)}")
    print(f"Greatest Increase in Profits: {G_Increase_Month} (${G_Increase})")
    print(f"Greatest Decrease in Profits: {G_Decrease_Month} (${G_Decrease})")

#Creates a new textfile and writes the output to that file    
output_file = os.path.join("budget_data_output.txt")

w = open('budget_data_output.txt','w')
w.write(f"Total Months: {len(months)}")
w.write(f"\nTotal: $ {(sum(amount))}")
w.write(f"\nAverage Change: $ {(average_change)}")
w.write(f"\nGreatest Increase in Profits: {G_Increase_Month} (${G_Increase})")
w.write(f"\nGreatest Decrease in Profits: {G_Decrease_Month} (${G_Decrease})")
w.close()
    
    
    
    
    
    
    