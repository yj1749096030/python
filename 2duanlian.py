

#1
import random
s1 = [chr(ord('A')+i) for i in range(26)]
s2 = [chr(ord('a')+i) for i in range(26)]
s3 = [str(i) for i in range(0,10)]
s4 = s1 + s2+ s3
print(s4)
def mm():
	s5 = [s4[random.randint(0,len(s4)-1)] for i in range(8)]
	return s5
for i in range(10):
	s5 = mm()
	s = ''
	for j in s5:
		print(s+j, end = '')
	print()

#2
import random
s = [random.randint(0,100) for i in range(20)]
print(s)
s1 = [0] * 11
for i in s:
	s1[i // 10] += 1
print(s1)
print('100:{}'.format(s[11]*'*'))
for i in range(9,-1,-1):
	print('{}~{}:{}'.format(i*10, 1*10+9, s1[i]*'*'))


#3
i = 0
while i < 10:
	try:
		s = int(input('1~100shuzi:'))
		if not 0 <= s <= 100:
			print('1~100')
			continue
	except Exception:
		print('shuzi')
		continue
	i += 1


mouth, year = eval(input('yue ,nian:'))
def run(year):
	if year % 4 == 0 and year % 100 != 100 or year % 400 == 0:
		return 1
	else:
		return 0
#print(run(1991))
days = 0
for i in range(1990,year):
	days += 365 + run(i)
#print(days)

def yue(mouth):
	if mouth in (1,3,5,7,8,10,12):
		return 31
	if mouth in(4,6,9,11):
		return 30
	if mouth == 2:
		return 28 + run(year)
for i in range(1,mouth):
	days += yue(i)
print(days)
days = days + 1
week = days % 7
print(week)
s = '{}月{}'.format(mouth, year)
print(s.center(20))
print('日 一 二 三 四 五 六')
print('{}'.format('   '*week), end = '')
for i in range(1,yue(mouth)+1):
	print('{:>2}'.format(i), end = '\n' if (i + week)%7 == 0 else ' ')
print()

mouth, year = eval(input('yue,nian:'))
def run(year):
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		return 1
	else:
		return 0
days = 0
for i in range(1990, year):
	days += 365 + run(year)
def yue(mouth):
	if mouth in (1,3,5,7,8,10,12):
		return 31
	if mouth in (4,6,9,11):
		return 30
	if mouth == 2:
		return 28 + run(year)
for i in range(1, mouth):
	days += yue(i)
days = days + 1
week = days % 7
print('{}月{}'.format(mouth, year))
print('日 一 二 三 四 五 六')
print('{}'.format('   '*week), end = '')
for i in range(1,yue(mouth) + 1):
	print('{:>2}'.format(i), end = '\n' if (week + i)% 7 == 0 else ' ')
print()

def huiw(s):
	if len(s) == 0:
		return True
	else:
		if s[0] == s[-1]:
			return huiw(s[1,-1]) 
		else:
			return False

s = 0
for i in range(100, 1001):
	for j in range(2,i):
		if i % j == 0:
			break
	else:
		s += 1
print(s)
