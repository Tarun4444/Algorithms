
def recursiveFun3(n):
    if n <= 0:
        return 1
    else:
        return 1 + recursiveFun3(n/5)

print(recursiveFun3(1))
