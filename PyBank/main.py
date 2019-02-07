import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
#setting up lists,and variables
total = 0
months = []
total_profit_loss = []   
max_change = 0
min_change = 0
change = []
min_i = 0
max_i = 0

#opening and reading file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

#appending lists, counting rows and total months 
    for row in csv.reader(csvfile):
        total_profit_loss.append(int(row[1]))
        months.append(row[0]) 
        months_total = len(months)
        total += int(row[1])
    
 #creating range and looping for max and min total profit lost   
    for i in range(1, len(total_profit_loss)):
        change.append(total_profit_loss[i] - total_profit_loss[i-1])
        average_change = round(sum(change)/len(change),2) 
        max_change = max(change)
        min_change = min(change)

 #creating range and looping to match month to max and min profit lost 
    for i in range(1, len(total_profit_loss)):
        if total_profit_loss[i] > total_profit_loss[max_i]:
           max_i = i
        max_months = months[max_i]
        if total_profit_loss[i] < total_profit_loss[min_i]:
           min_i = i
        min_months = months[min_i]

#printing results 
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {str(months_total)}")
    print(f"Total: ${(total)}")
    print(f"Average  Change: ${(average_change)}")
    print(f"Greatest Increase in profits: {max_months}, (${max_change})")
    print(f"Greatest Decrease in profits: {min_months}, (${(min_change)})")

#saving results to file
output_path = os.path.join("..", "PyBank", "results.txt")

with open(output_path, 'w', newline='') as datafile:

    csvwriter = csv.writer(datafile, delimiter=',')
    csvwriter.writerow([(f"Financial Analysis")])
    csvwriter.writerow([(f"----------------------------")])
    csvwriter.writerow([(f"Total Months: {str(months_total)}")])
    csvwriter.writerow([(f"Total: ${(total)}")])
    csvwriter.writerow([(f"Average  Change: ${(average_change)}")])
    csvwriter.writerow([(f"Greatest Increase in profits: {max_months} (${max_change})")])
    csvwriter.writerow([(f"Greatest Decrease in profits: {min_months} (${(min_change)})")])