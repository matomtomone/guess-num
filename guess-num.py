import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('猜對囉!')
		print('猜了', count, '次')
		break
	elif num < r:
		print('太小了')
	elif num > r:
		print('太大了')
	print('猜了', count, '次')