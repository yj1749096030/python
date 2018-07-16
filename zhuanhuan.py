
s = input("输入一个字符串：")
i = 0
while i < len(s):
	if ord(s[i]) < ord("a"):
		print(chr(ord(s[i]) + (ord("a") - ord("A"))))
	else:
		print(chr(ord(s[i]) - (ord("a") - ord("A"))))
	i += 1
