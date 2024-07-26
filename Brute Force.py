def find_brute_force(t, p):
    n, m = len(t), len(p)
    for i in range(n-m+1):
        k = 0
        while k < m and t[i+k] == p[k]:
            k += 1
        if k == m:
            return i
    return -1

text = "THIS IS A TEST TEXT"
pat = "TEST"
print(find_brute_force(text, pat))