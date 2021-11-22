# Zadanie 1
shop_dict=dict()
shop_dict['cukiernia']=['chałka', 'pączek', 'bułki']
shop_dict['warzywniak']=['marchew', 'seler', 'pietruszka','ziemniaki']
print('Lista zakupów')
count=0
for sklep in shop_dict:
    if isinstance(shop_dict[sklep],list):
       count+=len(shop_dict[sklep])
    print('Idę do '+sklep.capitalize()+', kupuję następujące rzeczy:'+repr(shop_dict[sklep]).title())
print('W sumie kupuję '+repr(count)+' produktów')

