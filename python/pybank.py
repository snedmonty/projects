import csv
total_months=total_revenue=change=previous_rev=0
changelog=[]
tracked={'rev_increase':0,'rev_decrease':0,'inc_month':"",'dec_month':""}
myfile = open("budget.csv", "r")
spreadsheet=csv.DictReader(myfile)
for row in spreadsheet:
    total_months+=1
    total_revenue+=int(row['Profit/Losses'])
    change=int(row['Profit/Losses'])-previous_rev
    previous_rev=int(row['Profit/Losses'])
    if change>tracked['rev_increase']:
        tracked['rev_increase']=change
        tracked['inc_month']=row['Date']
    elif change<tracked['rev_decrease']:
        tracked['rev_decrease']=change
        tracked['dec_month']=row['Date']
    changelog.append(change)
print(tracked['rev_decrease'])    
changelog.pop(0)
averagechange=sum(changelog)/(total_months-1)

report = "Financial Analysis\n----------------------------\nTotal Months: "+str(total_months)+"\nTotal: $"+str(total_revenue)
report+="\nAverage  Change: $"+str(round(averagechange,2))
report+="\nGreatest Increase in Profits: Year->"+tracked['inc_month']+ " Amount->$"+str(tracked['rev_increase'])+"\nGreatest Decrease in Profits: Year->"+tracked['dec_month']+ " Amount->$"+str(tracked['rev_decrease'])
print(report)

f = open("resultfile.txt", "w")
f.write(report)