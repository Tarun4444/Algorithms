#code
def balanced(a, n):
    b= []
    for i in range(n):
        if a[i] == '[' or a[i] == '{' or a[i] == '(':
            b.insert(0, a[i])
        else:
            if len(b) > 0:
                c = b[0]
                if c == '[' and a[i] == ']':
                    b = b[1:]
                    continue
                elif c == '{' and a[i] == '}':
                    b = b[1:]
                    continue
                elif c == '(' and a[i] == ')':
                    b = b[1:]
                    continue
                else:
                    return "not balanced"
            else:
                return "not balanced"
    return "balanced"


t=int(input())
while t > 0:
    a = list(input())
    n = len(a)
    print(balanced(a, n))
    t = t - 1