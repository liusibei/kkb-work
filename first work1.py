income = []
expenditure = []
everyday = {}
f = 0
n = 1
for i in range(0,7):
    a = int(input(f'请输入第{n}天的收入'))
    b = int(input(f'请输入第{n}天的支出'))
    income.append(a)
    expenditure.append(b)
    everyday[n] = a-b
    n+=1
for i in range(1,8):
    f = f+everyday[i]
print(f'7天的收入{income}')
print(f'7天的支出{expenditure}')
print(f'每天的结余{everyday}')
print(f'最终的结余{f}')
