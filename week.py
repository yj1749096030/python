s1 = "good evening"
s2 = "nice"
if s2 not in s1:
	print( 's2, "不在"， s1, "中"')
else:
	print('s2, "在", s1, "中"')
print(s1[0:5:3])
print(s1[0:5:4])
print(s1[5:9:3])
print(s1[5:10:2])

week = "星期一星期二星期三星期四星期五星期六星期日"
num = int(input("请输入1～7的数字："))
pos = (num - 1)*3
print(week[pos:pos+3])
