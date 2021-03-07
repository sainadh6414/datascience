num = 5
print(id(num))

num = 2.5;
print(type(num))

num=5;
print(type(num))

num = 6+9j
print(type(num))

a = 5.6
b = int(a)
print(type(b))

k = float(b)
print(type(k))

k = 6;
c = complex(b,k)
print(c)

print(b<k)

bl = b<k
print(bl)
print(type(bl))

lst = [25, 35, 45, 65]
print(type(lst))

st = {23, 23, 45, 45}
print(type(st))

tu = (23, 23, 45, 45)
print(type(tu))

str = 'name'
print(type(str))

print(range(0, 10))

print(list(range(10)))

print(list(range(2, 10, 2)))

dt = {'a' : 1};
print(type(dt))
print(dt['a'])
print(dt.keys())
print(dt.values())
print(dt.get('a'))

x = 2
y = 3
print(x+y)

x = x + 2
x +=2
print(x)

x*=3
print(x)

a,b=5,6
print(a, b)

n=7
print(-n)

print(a<b)
print(a>b)
print(a==b)
a=6
print(a==b)
print(a<=b)
print(a>=b)
a=10
print(a!=b)

t,f=True,False
print(t&f)
print(t|f)

print(bin(25)) #convert to binary

# If condition 
if True:
    print('I am right')
    print('I am in if condition')

x = 3
r = x%2

#if else elif

x =3
r = x%2
if r == 0:
    print('Even')
elif r == 1:
    print('Odd')
else:
    print('Niether even nor odd')

#while
while x != 3:
    print('awesome')

#for
y = [1, 2 ,3, 4]
for i in y:
    print(i)


