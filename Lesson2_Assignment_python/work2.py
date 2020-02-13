balance = 1000
while 1:
    print('''
    查询余额
    存款
    取款
    退出
    请输入你的操作''')
    operation = input()
    if operation == '查询余额':
        print(f'您的余额为{balance}')
        continue
    elif operation == '存款':
        number1 = int(input('请输入存款金额'))
        balance += number1
        continue
    elif operation == '取款':
        number2 = int(input('请输入取款金额'))
        if number2 <= balance:
            print('请取走现金')
            balance -= number2
        else:
            print('余额不足')
        continue
    elif operation == '退出':
        print('请取走你的卡片')
    else:
        print('请输入正确操作')
        continue
    break
