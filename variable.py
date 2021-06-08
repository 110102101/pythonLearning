peoples = 1001
area = 100

# check how much area each person occupys

areaPerPerson = peoples / area
print("there are %d peoples in wuTuoBang, and the all living area is %d,so each person in wuTuoBang occupys %10.2f." %
      (peoples, area, areaPerPerson))


# three children share 19 tangyuan, how many tangyuan left
childrenNumber = 3
tangyuanNumber = 19

leftTangyuan = 19 % 3
print("tangyuan left is %d" % leftTangyuan)

# and each child get how many tangyuan
tangyuanPerChild = tangyuanNumber // childrenNumber
print("each child get %d tangyuan" % tangyuanPerChild)


'''
other operator include :
	boolean operator : and / or / not

	binary operator: % | ~ ^ >> << (and or not xor leftShift rightShift)

	Identity operators:is / is not (refer to the same object or not)
	Membership operators: in / not in(this opertor is capital sensitive,and use key in dictionary)
'''

x = 8  # 0000 100
y = x << 5
print(" 8 left shift 5 bit is %d" % y)


a = 2
b = 2
p = a is b
print(" a is b that is %r " % p)


a = [1, 2, 3]
b = [1, 2, 3]
p = a is b
print(" a is b that is %r " % p)

dic = { 1:"hello",2:"world"}
number1isInDic = 1 in dic
hisInDic = "H" in dic
print("1 is in dic is %r" %number1isInDic)
print("H is in dic is %r" %hisInDic)
