# print('kira')
# a = 5
# b=10
# c=a+b
#
# print('the sum is ',c)
# s="kira"
# print(s[1:3])

# d= input('enter something: ')
#
# e=input('enter otherthing: ')
#
# print('your result: ',int(d)+int(e))
# kira = [1,22,3,4,5,66,7,8,9,0]
# print(kira)
# #
# # kira.sort()
# #
# # print(kira)
# #
# # kira.insert(0,2)
# #
# # print(kira)

kira={12,11,22}

kira.pop()
print(kira)

kp={
    "name" : "kira",
    "age" : 22
}

print(kp.get("name"))

if(2==4):
    print('no')

print('ad')


for a in range(5,2,-1):
    print(a)

def ap(n):
    if(n==1):
        return 1
    else:
        return n*ap(n-1)


num = int(input('enter \n'))
if(num<0):
    print('fact doesnot exist')
elif(num==0):
    print("fact=1")
else:
    print("factorial is",ap(num))
