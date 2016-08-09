import re
data = [
    'c15103','c155104','c15202',
    'n16001','n16002','n16003','n16004','n16005','n16006','n16007','n16008','n16009',
    'n16001','n16002','n16003','n16004','n16005','n16006','n16007',
    's16001','s16002','s16003','s16004','s16005','s16006','s16007','s16008','s16009',
]

str_data = str(data)
print(re.findall(r'c15[12]]0[342]',str_data))
print(re.findall(r'c15\d(3)',str_(data)))
print(re.findall(r'n16(1)\d(2)',str_(data))