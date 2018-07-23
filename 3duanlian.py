

import random
import string
s = string.ascii_letters + string.digits
#print(s)
y = len(s)
i = [s[random.randint(0,len(s)-1)] for i in range(8)]
print(i)
mm = [random.choice(s) for i in range(8)]
print(mm)



import random
s = [random.randint(0,100) for i in range(20)]
#print(s)
s1 = [0] * 11
for i in s:
	s1[i // 10] += 1
print(s1)
print('100:{}'.format(s1[10] * '*'))
for i in range(9,-1,-1):
	print('{}~{}:{}'.format(s[i] * 10, s[i] * 10 + 9, s1[i] * '*'))



import random
s = [random.randint(0,100) for i in range(20)]
s1 = [0] * 11
for i in s:
	s1[i // 10] += 1
print('100:{}'.format(s1[10] * '*'))
for i in range(9,-1,-1):
	print('{}~{}:{}'.format(s[i] * 10, s[i] * 10 + 1, s1[i] * '*'))



import random
y = random.randint(0,9)
i = 0
while i < 3:
	try:
		s = int(input('0~10:'))
		if not 0 <= s <= 10:
			continue
	except Exception:
		print('shuzi:')
		continue
	else:
		if s == y:
			print('dui,{}ci'.format(i))
			break
		elif s < y:
			print('xiao,hai you{}ci'.format(3 - (i + 1)))
		else:
			print('da,hai you{}ci'.format(3 - (i + 1)))
		i += 1
		

3个红球，3个蓝球，4个黄球



s = 0
for red in range(1,4):
	for blue in range(1,4):
		for yellow in range(1,5):
			if red + blue + yellow == 8:
				s += 1
				print('red:{},blue:{},yellow:{}'.format(red, blue, yellow))
print('gong{}jieg'.format(s))



for i in range(1,10):
	for j in range(1,i + 1):
		print('{} * {} = {}'.format(j, i , j*i), end = ' ')
	print()




for i in range(1,10):
	for j in range(1,i + 1):
		print('{} * {} = {}'.format(j, i, j*i), end = ' ')
	print()



def suma(s):
	if s == 0:
		return 0
	else:
		return s + suma(s - 1)
print(suma(1))



#rili
def run(year):
	if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
		return 1
	else:
		return 0
def day(mouth):
	if mouth in (1,3,5,7,8,10,12):
		return 31
	if mouth in (4,6,9,11):
		return 30
	if mouth == 2:
		return 28 + run(year)
mouth, year = eval(input('yue,nian:'))
days = 0
for i in range(1990,year):
	days += 365 + run(i)
for i in range(1,mouth):
	days += day(i)
days = days + 1
week = days % 7
#print(week)
s = '{}月{}'.format(mouth,year)
print(s.center(20))
print('日 一 二 三 四 五 六')
print('{}'.format('   ' * week), end = '')
for i in range(1,day(mouth) + 1):
	print('{:>2}'.format(i), end = '\n' if (i + week) % 7 == 0 else ' ')
print()



s1, s2 = input('zifuch:').split()
if s1 == s2:
	print('=')
else:
	i = 0
	j = 0
	while i < len(s1) and j < len(s2):
		if s1[i] > s2[j]:
			print('>')
			break
		elif s1[i] < s2[j]:
			print('<')
			break
		elif s1[i] == s2[j]:
			i += 1
			j += 1
	else:
		if len(s1) > len(s2):
			print('>')
		else:
			print('<')



s = input('zfch:')
flag = True
for i in s:
	if ord('A') <= ord(i) <= ord('z') and flag:
		print(i.upper(),end = '')
		flag = False
	else:
		if ord('A') <= ord(i) <= ord('z') and flag == False:
			print(i, end = '')
		if i == ' ':
			flag = True
print()
		


s = input('zfch:')
flag = True
for i in s:
	if ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z') and flag:
		print(i.upper(), end = '')
		flag = False
	elif i == ' ':
		flag = True
	elif flag == False and ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z'):
		print(i, end = '')
print()



import time
print('start')
for i in range(11):
	print('\r{}%{}{}'.format(i * 10, i * '#', (10 - i) * '-'), end = '')
	time.sleep(0.5)
print()
print('end')



import time
print('start')
for i in range(11):
	print('\r{:>3}%{}{}'.format(i * 10, i * '#', (10 - i) * '-'), end = '')
	time.sleep(0.5)
print()
print('end')


import string
import random
s = string.ascii_letters + string.digits
#print(s)
for j in range(10):
	s1 = ''
	for i in range(8):
		s1 += random.choice(s)
	print(s1)




