

'''
while True:
	s = input('zfch:')
	if len(s) > 5:
		print('again')
	else:
		print('nice')
		break
'''

'''
#dayup

dayup = 1
daydown = 1
dayup2 = 1
s = 1
for i in range(1, 366):
	s = s * (1+0.01)
	if i % 7 == 0:
		dayup = dayup * (1 - 0.01)
	else:
		dayup = dayup * (1 + 0.01)
daydown = daydown * (1-0.01)**365
dayup2 = dayup2 * (1+ 0.01)**365
print(dayup, dayup2, daydown)
print(s)
'''
'''
week = "星期一星期二星期三星期四星期五星期六星期日"

s = int(input('1~7shu:'))
i = (s-1)*3
print(week[i:i+3])
'''

'''
s1, s2 = input('2zifuchuan:').split()
i = len(s1)
j = len(s2)
if i>j:
	q=s2
if i<j:
	q=s1
if s1 == s2:
	print('=')
else:
	for w in range(len(q)):
		if ord(s1[w]) > ord(s2[w]):
			print('>')
			break
		elif ord(s1[w]) < ord(s2[w]):
			print('<')
			break
	else:
		print(q,'<')
		
'''

'''
s1, s2 = input('2zfch:').split()
i = 0
j = 0
flag = True
while i<len(s1) and j<len(s2):
	if ord(s1[i]) < ord(s2[i]):
		print('<')
		flag = False
		break
	elif ord(s1[i]) > ord(s2[i]):
		print('>')
		flag = False
		break
	else:
		i += 1
		j += 1
if s1 == s2 and flag:
	print('=')
elif len(s1) > len(s2) and flag:
	print(s1,'>',s2)
elif len(s1) < len(s2) and flag:
	print(s1,'<', s2)
'''	

s = input('zfch:')
flag = True
for i in s:
	if ord(A)<= i<=ord(Z):
		print(i, end='')
	elif 
		print(chr(ord(i)-32), end='')






















