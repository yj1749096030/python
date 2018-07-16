
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
elif s1[q-1] == s2[q-1]:
	print(y, '<', j)
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





