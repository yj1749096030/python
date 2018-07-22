

#1
import random
l1 = []
for i in range(10):
	l1.append(random.randint(1,100))
print(l1)
s = 0
def sumall(n):
	global s
	for i in l1:
		s = (s + i)
	a = s/10
	b = max(l1)
	c = min(l1)
	n = [a,b,c]
	return n
print(sumall(l1))
 

#2
l2 = [random.randint(1,10) for i in range(10)]
print(l2)
s = max(l2)
l2.remove(s)
l2.append(s)
print(l2)

#3
l3 = 'qwertyuioplkjhgfdsazxcvbnm'
l4 = [i for i in l3]
#print(l4)
l5 = [0,1,2,3,4,5,6,7,8,9]
l6 = l4 + l5
#print(l6)
l7 = l3.upper()
#print(l7)
l8 = [i for i in l7]
l9 = l8 + l6
#print(l9)
l10 = l9.copy()
def mima(n):
	m = len(n)
	for i in range(8):
		n.append(n[random.randint(0,m-1)])
	j = n.copy()
	del j[0:m]
	return j
for i in range(10):
	print(mima(l10))



#4

def sj(n):
	s = [random.randint(0,100) for i in range(20)]
	n = s.copy()
	return n
s = sj(n=[])
print(s)	
def yy(n):
	global s
	cut = 0
	for i in n:
		if i in s:
			cut += 1
	return cut
#print(yy(range(11)))
m = '*'	









