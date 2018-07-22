
def nixu(s):
	if s == '':
		return ''
	return nixu(s[1:]) + s[0]
print(nixu('python'))

def suma(s):
	if s==0 or s==1:
		return s
	return s + suma(s-1)
print(suma(100))








s = [11,22,33,44,55]
y = [66,77,88,99,00]
print(s[1:4])
print(s[::2])
print(s[0::2])
print(s.index(22,1,-1))

z = []
z.append(12)
z.append(13)
print(z)
z.insert(1,20)
l = z.copy()
print(z,l)
l1 = l
l.extend(l1)
print(l,l1)
l.reverse()
print(l,l1)
l = sorted(l)
z.sort()
print(l,z)
x = z.sort()
print(x)
x = l[-2:-1]
print(x)

l2 = [i*i for i in range(1,11,2)]
print(l2)
l3 = [i*i for i in range(1,11) if i%2]
print(l3)
print('ji' if 4%2 else 'ou')

h = 'ABCD'
j = 'MNOP'
l4 = []
for i in h:
	for k in j:
		l4.append(i+k)
print(l4)

l.reverse()
print(l)





