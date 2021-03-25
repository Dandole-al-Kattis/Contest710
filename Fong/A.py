
def solve(n, m, x):
    i = (x-1)//n
    j = x-(i*n+1)
    return i+m*j+1


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n, m, x = list(map(int, input().split()))
        print(solve(n, m, x))
