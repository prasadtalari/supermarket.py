from datetime import datetime

name=input("Enter your name:")


lists='''
Rice    Rs  20/kg
sugar   Rs  30/kg
oil     Rs  50/liter
paneer  Rs  70/kg
salt    Rs  40/kg
maggie  Rs  50/kg
boost   Rs  90/each
colgate Rs  85/each
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,'sugar':30,'oil':50,'paneer':70,'salt':40,'maggie':50,
'boost':90, 'colgate':85}
option=int(input("for list of items press1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
       break
    if inp1==1:
        item=input("Enter your items")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])  
            pricelist.append((item,quantity,items,price))  
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
            print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp== 'yes':
        pass
    if finalamount!=0:
            print(25*"=","prasad supermarket",25*"=")
            print(28*"","serilingampally")  
            print("name:",name,30*" ""date:",datetime.now())  
            print(75*"=")
            print("sno",8*"," 'items',8*","'quantity',3*" "'price')
            for i in range(len(pricelist)):
              print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
              print(75*"-")
              print(50*" ",'totalamount:','rs',totalprice)
              print(75*"-")
              print(50*" ",'finalamount:','rs',finalamount)
              print(75*"-")
              print(50*" ","thanks for visiting")
              print(75*"-")                        
