import os
import csv
import sys

# Specify csv file path
csv_path = os.path.join("Resources","budget_data.csv")

# Open and read csv file skipping header row

with open(csv_path, 'r') as csv_file:

    budget_data = csv.reader(csv_file,delimiter=',')

    next(budget_data)

# Create lists for month and correspoding profit/loss data from the csv file

    month=[]
    profit_loss =[]

    for row in budget_data:

        month.append(row[0])
        profit_loss.append(int(row[1]))

# print total months & calculate & print net profit/loss

    print("Financial Analysis")

    print("------------------------------")

    print("Total Months:" + str(len(month)))

    Total=sum(profit_loss)

    print("Total: $"+str(Total))

# calculate the changes in profit/loss for each month and create a list

    difference=[]

    for n in range(85):

        difference_1 = profit_loss[n+1]-profit_loss[n]
        difference.append(difference_1)

# Calculate the changes in profit/loss over the entire period & the average

    difference_sum=sum(difference)
    average_differecne= round(difference_sum/85,2)
    print("Average Change: $" + str(average_differecne))

# Create a list of months to correspond to the changes in profit/loss

    month_difference=[]
    for index in month[1:]:
        month_difference.append(index)

# Create dictionary and find the greatest increase and decrease in profits

    difference_dictionary=dict(zip(month_difference,difference))
    greatest_increase=max(difference)
    greatest_decrease=min(difference)

# Find the corresponding months for the greatest increase and decrease in profits by looking through dictionary values and keys

    for key, value in difference_dictionary.items():

        if value == greatest_increase:

            increase_month = key
            increase = value
        
        elif value == greatest_decrease:

            decrease_month = key
            decrease = value

            

    print("Greatest Increase in Profits: "+ str(increase_month)+" "+"("+str(increase)+")")
    print("Greatest Decrease in Profits: "+ str(decrease_month)+" "+"("+str(decrease)+")")

# Export to txt file

output_path = os.path.join("analysis","analysis.txt")

with open(output_path, "w") as txt_file:

    print("Financial Analysis", file=txt_file)

    print("------------------------------", file=txt_file)

    print("Total Months:" + str(len(month)), file=txt_file)
    print("Total: $"+str(Total), file=txt_file)
    print("Average Change: $" + str(average_differecne), file=txt_file)
    print("Greatest Increase in Profits: "+ str(increase_month)+" "+"("+str(increase)+")", file=txt_file)
    print("Greatest Decrease in Profits: "+ str(decrease_month)+" "+"("+str(decrease)+")", file=txt_file)

