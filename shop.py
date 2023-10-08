items={'laptop':[30000,10],"mouse":[100,5],"monitor":[4000,3]}
print("Available items:-")
for i in items:
    print("Item name: ",i,end=", ")
    print("Price: ",items[i][0],end=", ")
    print("Avilable Quantity: ",items[i][1])
p=0
order={}
while True:
    print("Enter 'e' to exit.")
    item=input("Enter the name of the product you want to buy: ")
    if item=="e":
        break
    q=int(input("Enter the quantity: "))
    if q>items[item][1]:
        print("Out of stock.")
        continue
    items[item][1]-=q
    order[item]=q

if order!={}:
    tp=0
    print("===================Bill===================")
    print("Item Name        Quantity        Price")
    for i in order:
        p=items[i][0]*order[i]
        print(i,end="               ")
        print(items[i][1],end="            ")
        print(p)
        tp+=p
    print("------------------------------------------")
    print("Total Price:                      ",tp)
    print(items)
print("Thank You")


