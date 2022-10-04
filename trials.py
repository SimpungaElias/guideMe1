head = "Hello, Welcome to elHalal here's our menu. "
print(head)
g1 = 'Burger'
g2 = 'Soda'
print(g1, 'and', g2)
BURGER = g1
SODA = g2
COST_OF_BURGER = 3.0
COST_OF_SODA = 2.0
def myGoods(prompt, burger, soda):
    while True:
        goods = input(prompt)
        try:
            goods = str(goods)
        except:
            print('That is not my goods, please try again.')
            continue
        if (myGoods != g1 ) or (myGoods !=  g2):
            print('The goods you entered is ', burger, 'and', soda)
        else:
            
            return goods
Goods = myGoods('Please enter the product: ')
print(' The product you entered was: ',Goods)
good1 = str(input('Please enter  what you want: '))
value1 = int(input('Please Enter the cost of burger : '))
good2 = str(input('Please enter another thing you want: '))
value2 = int(input('Please Enter the cost of soda: '))
cashPaid = 10
def calcChange(n1,n2):
    total = n1 + n2
    change = cashPaid - total
    return change
answer = 'y'
while answer == 'y':
    users = str(input('continue...'))
    #print('users')
    answer = input('Do you want to order again?(y or n): ')
total = value1 + value2
value1 = value1
value2 = value2
changeValue = calcChange(value1, value2)
print('Total is: ', total)
print('You paid', cashPaid, 'and the change is', changeValue, 'Thank you, Always comeback!')


