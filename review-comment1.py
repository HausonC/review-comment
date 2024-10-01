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

print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	count += 1
	if count % 10000 == 0:
# 		print(sum_len)

print('the avg lenth of comment', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('total', len(new), 'data whose lengths are less than 100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
good = [d for a in data if 'good' in d] # list comprehension: replace rows 37-40
print('total', len(good), 'data with GOOD comment')
print(good[0])
print(good[1])

bad = []
for d in data:
	bad.append('bad' in d)
#bad = ['bad' in d for d in data] # same as rows 46 - 48
print(bad) # if comment include 'BAD' then print True, otherwise print False

# count word volume
word_count = {}
for d in data:
	words = d.split() # split(' ') = split()
	for word in words:	# nest for loop
		if word in word_count:
			word_count[word] += 1 # if a word exists in word_count. counter +1
		else:
			word_count[word] = 1
for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word])

print(len(word_count))
print(word_count['Allen'])

while True:
	word = input('please input a word you want to look up:')
	if word == 'q': 
		print('thanks for using')
		break
	if word in word_count:
		print(word, 'the appearance count is:', word_count[word])
	else:
		print('this word never exists')	

# x = int(len(data))
# print(x)
# print('')
# print('1st comment')
# print(data[0]) 		# print the 1st data in 'data' list
# print('')
# print('the last comment')
# print(data[x-1])