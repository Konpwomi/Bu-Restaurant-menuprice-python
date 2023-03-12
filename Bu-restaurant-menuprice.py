print ('''.................................................
                  BU Restaurant
                       Menu
.................................................
Menu ID                Menu                Price
  F01          Tuna Tartare Salsa            125
  F02          Cordon Bleu Chicken           145
  F03          Salmon Steak with Sauce       169
  F04          Caesar Salad                  139
  D01          Sparkling Sunset               90
  D02          Coke Mojito                    60
.................................................''')

menuID = ['F01','F02','F03','F04','D01','D02']
menuList = ['Tuna Tartare Salsa','Cordon Bleu Chicken','Salmon Steak with Sauce','Caesar Salad','Sparkling Sunset','Coke Mojito']
menuPrice = ['125','145','169','139','90','60']

choice = []
quantList = []
price = []

food = []
drink = []

menu = input('Enter menu ID : ')

x=0
while menu in menuID :
    qua = int(input('Enter quantity : '))
    if menu  == 'F01' :
        choice.append(menuList[0])
        quantList.append(qua)
        price.append(qua*125)
        food.append(price[x])
    elif menu == 'F02' :
        choice.append(menuList[1])
        quantList.append(qua)
        price.append(qua*145)
        food.append(price[x])
    elif menu == 'F03' :
        choice.append(menuList[2])
        quantList.append(qua)
        price.append(qua*169)
        food.append(price[x])
    elif menu == 'F04' :
        choice.append(menuList[3])
        quantList.append(qua)
        price.append(qua*139)
        food.append(price[x])
    elif menu == 'D01' :
        choice.append(menuList[4])
        quantList.append(qua)
        price.append(qua*90)
        drink.append(price[x])
    elif menu == 'D02' :
        choice.append(menuList[5])
        quantList.append(qua)
        price.append(qua*60)
        drink.append(price[x])
    x+=1
    ans = input('Quit (Y/N) : ')
    if ans == 'N' :
        pass
    elif ans == 'Y' :
        break   
    print(' ')
    menu = input('Enter menu ID : ')
else :
    print("Invalid Code! Please try again.")
    menu = input('Enter menu ID : ')
    while menu in menuID :
        qua = int(input('Enter quantity : '))
        if menu  == 'F01' :
            choice.append(menuList[0])
            quantList.append(qua)
            price.append(qua*125)
            food.append(price[x])
        elif menu == 'F02' :
            choice.append(menuList[1])
            quantList.append(qua)
            price.append(qua*145)
            food.append(price[x])
        elif menu == 'F03' :
            choice.append(menuList[2])
            quantList.append(qua)
            price.append(qua*169)
            food.append(price[x])
        elif menu == 'F04' :
            choice.append(menuList[3])
            quantList.append(qua)
            price.append(qua*139)
            food.append(price[x])
        elif menu == 'D01' :
            choice.append(menuList[4])
            quantList.append(qua)
            price.append(qua*90)
            drink.append(price[x])
        elif menu == 'D02' :
            choice.append(menuList[5])
            quantList.append(qua)
            price.append(qua*60)
            drink.append(price[x])
        x+=1
        ans = input('Quit (Y/N) : ')
        if ans == 'N' :
            pass
        elif ans == 'Y' :
            break   
        print(' ')
        menu = input('Enter menu ID : ')

total = sum(food)+sum(drink)
tax = total*(0.07)

print ('.................................................')
ans = input('BU Member Card (Y/N) : ')

if ans == 'Y' :
    discount = -(sum(food)*(0.1))
else :
    discount = 0
subtotal = (total+discount+tax)

print ('''.................................................
                  BU Restaurant
                     receipt
.................................................
        menu              QTY            Price''')

x = 0
while x in range(len(choice)) :
   print(" %-26s%d              %3d" %(choice[x], quantList[x], price[x]))
   x += 1


print ('.................................................')
print("%-41s%7.2f" % ("Price", total))
print("%-41s%7.2f" % ("Discount (only food)", discount))
print("%-41s%7.2f" % ("Tax (7%)", tax))
print("%-41s%7.2f" % ("Total", subtotal))
print ('.................................................')