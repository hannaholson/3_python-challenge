import csv
with open('Resources/budget_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    lines= len(list(reader))
    print('Total Months:', lines)
    TotalProfitsLoss = 0
  
with open('Resources/budget_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')    
    for row in reader :
        TotalProfitsLoss = TotalProfitsLoss + int(row['Profit/Losses'])
        
    print('Total: $', TotalProfitsLoss)


with open('Resources/budget_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    Changes = 0
    First = int(next(reader)['Profit/Losses'])
    MaxIncrease = 0
    MaxDecrease = 0
    MaxIncreaseDate = "Date"
    MaxDecreaseDate = "Date"
    for row in reader:
        Changes = Changes + First - int(row['Profit/Losses'])
        if First - int(row['Profit/Losses']) > MaxIncrease:
            MaxIncrease = First - int(row['Profit/Losses'])
            MaxIncreaseDate = (row['Date'])

        if First - int(row['Profit/Losses']) < MaxDecrease:
            MaxDecrease = First - int(row['Profit/Losses'])
            MaxDecreaseDate = (row['Date'])
           
        First = int(row['Profit/Losses'])
       

    print('Average Change: $', Changes/lines)

    print('Greatest Increase in Profits: $', MaxIncrease, MaxIncreaseDate)
    print('Greatest Decrease in Profits: $', MaxDecrease, MaxDecreaseDate)

    
    

    
