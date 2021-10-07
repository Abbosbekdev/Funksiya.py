#1-masala

"""faktoryalni hisoblovchi rekursiv funksiya"""

# def fakt(a):
#     if a==1 :
#         return 1
#     else :
#         return a*fakt(a-1)
# a = int(input())
# print(fakt(a))

#2-masala

"""2 ga farq qiluvchi sonlar kopaytmasini topuvchi rekursiya"""

# def fakt2(a):
#     if a==0 or a==1 :
#         return 1
#     else :
#         return a*fakt2(a-2)
# a = int(input())
# print(fakt2(a))

#3-masala

""" sonni darajasini topuvchi rekursiya"""
# def daraja_kotar(x,n):
#     if x==0 or x==1 :
#         return 1
#     elif x%2==0 :
#         return daraja_kotar(n,x//2)*daraja_kotar(n,x//2)
#     elif x%2==1:
#         return n*daraja_kotar(n,x)
# x,n = int(input()),int(input())
# print(daraja_kotar(n,x))
 """xato ishladi xatosini topish kerak """

#4-masala

# def fib(a):
#     if a ==1 or a==2 :
#         return 1
#     else :
#         return fib(a-1)+fib(a-2)
# a = int(input())
#     print(fib(a))

#5-masala

# def fib(a):
#     if a ==1 or a==2 :
#         return 1
#     else :
#         return fib(a-1)+fib(a-2)
# a = int(input())
# for x in range(1,a+1) :
#     print(fib(x))

#6-masala

# def combin(n,k):
#     if n==0 or k==0 or n==k :
#         return 1;
#     else:
#         return combin(n-1,k)+combin(n-1,k-1)
# n,k = int(input()),int(input())
# print(combin(n,k))

#9-masala

"""2 sonni ekubini topuvchi rekursiv funksiya"""

# def ekub(a,b):
#     if b==0 :
#         return a
#     else:
#         return ekub(b,a%b)
# a,b = int(input()),int(input())
# print(ekub(a,b))

#10-masala

"""sonni raqamlari yig'indisini topuvchi rekursiv funksiya """
def summ_top(a):
    if a == 0 :
        return 0
    else:
        return summ_top(a//10)+a%10
a = int(input())
print(summ_top(a))
