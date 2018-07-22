
m, y = eval(input('输入1990年后的月，年'))
d = 0
#统计年的天数
for i in range(1990,y):
	d = d + 365 + (i%400==0)
#统计月的天数
for i in range(1, m):
	if i==1 or i==3 or i==7 or i==5 or i==8 or i==10 or i==12:
		d = d+31
	elif i==4 or i==6 or i==9 or i==11:
		d = d+30
	else:
		d = d + 28 + (y%400==0)
d = d+1
#月第一天是星期几
week = d % 7
z = "{}月{}".format(week, y)
print(z.center(20))
print('日 一 二 三 四 五 六')
#打印空格
for i in range(week):
	print("  ",end=' ')
#打印月的天数
mdays = 0
if m==1 or m==3 or m==7 or m==5 or m==8 or m==10 or m==12:
	mdays = 31
elif m==4 or m==6 or m==9 or m==11:
	mdays = 30
else:
	mdays = 28 + (y%400==0)
for i in range(1,mdays + 1):
	print('{:>2}'.format(i), end = "\n" if (week+i)%7==0 else " ")
print()









