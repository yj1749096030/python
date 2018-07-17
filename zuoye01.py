
'''
#1的作业

num1, num2 = eval(input("输入两个整形数："))
if num1 < num2:
	print(num1, '<', num2)
elif num1 == num2:
	print(num1, '=', num2)
else:
	print(num1, '>', num2)
'''

#2的作业

s1 = input('输入第一个字符串：')
s2 = input('输入第二个字符串：')
i = 0
if len(s1) > len(s2):
	y = s2 
	j = s1
else:
	y = s1 
	j = s2
q = len(y)
if s1 == s2:
	print(s1, '=', s2)
else:
	
	while i < len(y):
		if ord(s1[i]) > ord(s2[i]):
			print(s1, '>', s2)
			break
		elif ord(s1[i]) < ord(s2[i]):
			print(s1, '<', s2)
			break
		else:
			i += 1
	else:
		print(y, '<', j)
		

'''
#3的作业

y = input('输入一个字符串：')
i = 0
q = 0
w = 0
e = 0

while i < len(y):
	s = y[i]
	if s.islower():
		q += 1
	elif s.isdigit():
		w += 1
	elif s.isupper():
		e += 1
	i += 1
print("小写字母个数：", q)
print("大写字母个数：", w)
print("数写字母个数：", e)


#4的作业

s = input("输入一个字符串：")

print(s.title())


'''





































