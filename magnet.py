def force(idx, mid, a, n):
    f_x = 0
    for j in range(idx + 1):
        f_x += (1 / (a[j] - mid))

    for j in range(idx + 1, n):
        f_x += (1 / (a[j] - mid))

    return f_x


def magnet():
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))

        for i in range(n - 1):

            idx = i
            low = a[i]
            high = a[i + 1]

            while low < high:
                mid = (low + high) / 2
                f = force(idx, mid, a, n)

                if abs(f) <= 0.0000000000001:
                    print(("%0.2f" % (mid)), end=" ")
                    break

                elif f > 0:
                    high = mid

                elif f < 0:
                    low = mid
        t -= 1


if __name__=='__main__':
    magnet()