selling = int(input("enter the selling price: "))
cost = int(input("enter the cost price: "))

profit=selling-cost

print ("the profit is:",profit)
if profit < 0:
    print ("its a loss")