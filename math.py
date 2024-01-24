how = int(input())
a = [input() for i in range(how)]
b = [a[i] for i in range(how//2)]
c = [a[i] for i in range(how//2, how)]
print(b)
print(c)
