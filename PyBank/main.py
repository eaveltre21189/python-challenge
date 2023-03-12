import os
import csv

def my_format(my_values):
    return '${:,.2f}'.format(my_values)

budget_csv = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Analysis", "financial_analysis.txt")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)      

    month_count = 0
    pl_total = 0
    first_row = 0
    cur_chg = 0
    prev_chg = 0
    change_list = []
    month_change = []
    greatest_inc = ["", 1]
    greatest_dec = ["", 0]
    avg = 0

    for row in csv_reader:
        month_count += 1
        pl_total = pl_total + int(row[1])

        if first_row == 0:
            first_row = float(row[1])
        
        cur_chg = float(row[1]) - prev_chg
        prev_chg = float(row[1])

        change_list = change_list + [cur_chg]
        month_change = [month_change] + [row[0]]

        if cur_chg > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = cur_chg

        if cur_chg < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = cur_chg
    
    avg = ((sum(change_list)-first_row)/(len(change_list)-1))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total: {str(my_format(pl_total))}")
print(f"Average Change: {str(my_format(avg))}")
print(f"Greatest Increase in Profits: {greatest_inc[0]} ({str(my_format(greatest_inc[1]))})")
print(f"Greatest Decrease in Profits: {greatest_dec[0]} ({str(my_format(greatest_dec[1]))})")

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {str(month_count)}\n")
    file.write(f"Total: {str(my_format(pl_total))}\n")
    file.write(f"Average Change: {str(my_format(avg))}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc[0]} ({str(my_format(greatest_inc[1]))})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec[0]} ({str(my_format(greatest_dec[1]))})\n")
