data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0: 	# %: 求餘數
			print(len(data)) # follow row 7, 每讀1000筆印出一個數字 (顯示進度)
# print(len(data)) 	# print data length (資料筆數)
print('there are total', len(data), 'data')
x = int(len(data))
print(x)
print('')
print('1st comment')
print(data[0]) 		# print the 1st data in 'data' list
print('')
print('the last comment')
print(data[x-1])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	count += 1
	if count % 10000 == 0:
		print(sum_len)

print('the avg lenth of comment', sum_len/len(data))