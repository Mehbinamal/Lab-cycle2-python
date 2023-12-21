import pandas as pd
from tabulate import tabulate


def rabbit(n):
    total = [0]
    pair_rabbit_no = [1]
    rabbit_no = []
    month_no = []
    for i in range(n):
        rabbit_no.append(pair_rabbit_no[i]*2)
        total.append(pair_rabbit_no[i]), pair_rabbit_no.append(total[i] + pair_rabbit_no[i])
        month_no.append(i+1)
    return rabbit_no, month_no


a = int(input("Enter the month No: "))
list_rabbit, month = rabbit(a)
print("Month no \t Rabbit No")
for m in range(len(list_rabbit)):
    print(month[m], '\t\t\t\t', list_rabbit[m])


df = pd.DataFrame({'Month No': month, 'Rabbit No': list_rabbit})
print(df)
combined_list = list(zip(month, list_rabbit))
print(tabulate(combined_list, headers=['Month No', 'Rabbit no'], tablefmt="grid"))
