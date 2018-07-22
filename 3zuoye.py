
'''
#作业1
import random
i = random.randint(1, 10)
y = 0
while True:
	s = eval(input('输入一个整形数：'))
	if s==i:
		print('厉害了，500万属于你')
		break
	if s > i and y<2:
		print('大了，再给你一次机会')
	if s < i and y<2:
		print('大胆一点')
	y += 1
	if (s > i or s<i) and y==3:
		print('很遗憾，你没有中奖')
	if y == 3:
		break

'''

'''
while True:
	try:
		gess = int(input('输入一个10以内的整形数：'))
		Exception
		if gess>=10:
			raise Exception
	except Exception:
		print('again')
	else:
		break
'''

'''
for i in range(1,10):
	for j in range(1,i+1):
		print('{}*{}={}'.format(i,j,i*j), end= '\n' if i==j else ' ')
		print('{}*{}={}'.format(i,j,i*j),end=' ')
	print()
'''


'''
s=0
for red in range (1,4):
	for bule in range(1,4):
		for yellow in range(1,5):
			num = red+bule+yellow
			if num == 8:
				s =s+1
				print(red,bule,yellow)
print(s)
'''

'''
i =1
for j in range(10):
	i = (i+1)*2
print(i)
'''
'''
def pow(n, m):
	y = -1
	y = n**m
	return y
print(pow(2,3))
'''
'''
def big(num):
	i = num[0]
	q = len(num)
	for w in range(q):
		if ord(i)<=ord(num[w]):
			i == num[w]
	return num[w]
print(big('asdfg'))
'''
		
'''
def sum(n, m=2):
	return n**m
print(sum(5))
print(sum(3, m = 3))

def sum(*a):
	s = '0'
	for i in a:
		s=s+i
	return s
print(sum('s','m'))	
'''
'''
def test(a,b=2,*c):
	print(a,b)
	for i in c:
		print(i)
test(2,3,1,2,3)
'''

s1 = input("start:")
s2 = input("start:")
if s1==s2:
	print('=')



















