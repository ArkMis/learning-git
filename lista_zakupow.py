# Zadanie 1
shop_dict=dict()
shop_dict['piekarnia']=['chleb', 'pączek', 'bułki']
shop_dict['warzywniak']=['marchew', 'seler', 'rukola']
print('Lista zakupów')
count=0
for sklep in shop_dict:
    if isinstance(shop_dict[sklep],list):
       count+=len(shop_dict[sklep])
    print('Idę do '+sklep.capitalize()+', kupuję następujące rzeczy:'+repr(shop_dict[sklep]).title())
print('W sumie kupuję '+repr(count)+' produktów')

# Zadanie 2
numbers=[]
numbers3=[]
for x in range(0,101):
    if x%5==0:
        numbers.append(x)
print(numbers)
numbers3=[x**3 for x in numbers]
print(numbers3)

