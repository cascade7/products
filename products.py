import os

products = []
if os.path.isfile('products.csv'):
	print('找到了')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip('\n').split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
#	p = []  
#   p.append(name)
#	p.append(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格: ', p[1])

with open('products.csv', 'w', encoding='utf-8') as f :                         
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+','+p[1]+'\n')