import random
start = input('開始值')
end = input('結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
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