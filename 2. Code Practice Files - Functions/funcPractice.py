revenue = [10000,20000,30000,50000,100000]
expenses = [1000,5000,10000,15000,20000]
profit = [9000,15000,20000,35000,80000] # profit = revenue - expenses 

# WITHOUT FUNCTIONS
revenue_percentage_change = []
for i in range(1,len(revenue)): #len() -> No. of items in the list
    change = revenue[i]-revenue[i-1] 
    percentage_change = (change/revenue[i-1])*100
    revenue_percentage_change.append(percentage_change)
print('Revenue Percentage Change:')
print(revenue_percentage_change)

expenses_percentage_change = []
for i in range(1,len(expenses)):
    change = expenses[i]-expenses[i-1]
    percentage_change = (change/expenses[i-1])*100
    expenses_percentage_change.append(percentage_change)
print('Expenses Percentage Change:')
print(expenses_percentage_change)

profit_percentage_change = []
for i in range(1,len(expenses)):
    change = profit[i]-profit[i-1]
    percentage_change = (change/profit[i-1])*100
    profit_percentage_change.append(percentage_change)
print('Profit Percentage Change:')
print(profit_percentage_change)

print("\n")

# WITH FUNCTIONS - Reduce code duplication
def calculate_percentage_change(metric, name = 'Metric'): #Default value
    metric_percentage_change = []
    for i in range(1,len(metric)):
        change = metric[i]-metric[i-1]
        percentage_change = (change/metric[i-1])*100
        metric_percentage_change.append(percentage_change)
    print(name + ' Percentage Change:')
    print(metric_percentage_change)
 
calculate_percentage_change(revenue, 'Revenue')
calculate_percentage_change(expenses, 'Expenses')
calculate_percentage_change(profit, 'Profit')
print("\n")