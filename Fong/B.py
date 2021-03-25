def solve(n, k, s):
    #El primer y ultimo asterisco deben de ser intercambiados, ahi se llevan 2
    #Si la distancia entre el primer y el ultimo X es menor o igual que k.
    #Entonces termine.
    #En otro caso, me tengo que mover a aquel asterisco que mas distancia
    #abarque, ya sea a la derecha o a la izquierda y repito recursivamente.
    #regresado un movimiento mas de lo que regrese la llamada recursiva.
    i, j = 0, len(s)-1
    while i < len(s) and s[i] == '.':
        i += 1
    while j > -1 and s[j] == '.':
        j -= 1
    if j < i:
        return 0 #Only . in the string.
    if i == j:
        return 1 #Only one * in the string.
    else:
        s[i] = 'x'
        s[j] = 'x'
        return 2 + solve_rec(i, j, s, k)

def solve_rec(i, j, s, k):
    print(s)
    if j - i > k:
        return 0
    n = len(s)
    ip, ir = i+1, i
    while ip < len(s) and ip < i+k:
        if s[ip] == '*':
            ir = ip
        ip += 1
    jp, jr = j-1, j
    while jp >= 0 and jp > j-k:
        if s[jp] == '*':
            jr = jp
        jp -= 1
    if ir - i > j - jr:
        s[ir] = 'x'
        return 1 + solve_rec(ir, j, s, k)
    else:
        s[jr] = 'x'
        return 1 + solve_rec(i, jr, s, k)
    
        
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n, k = list(map(int, input().split()))
        s = list(input())
        print(solve(n, k, s))
