def fib(n):
    if n in [0,1]:
        return n
    return fib(n-1)+ fib(n-2)

num = int(input("Enter number...."))
n = 10
for i in range(n):
    sln= fib(i)
    if num == sln:
        print(num ,"is a fibonacci ")
        break
else:
    print(num, "is not a fibonacci ")