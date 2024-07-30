def find_kmp(t,p):
    n, m = len(t), len(p)
    if m == 0:
        return 0
    fail = compute_kmp_fail(p)
    j = 0
    k = 0
    while j<n:
        if t[j] == p[k]:
            if k == m-1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1

def compute_kmp_fail(p):
    m = len(p)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if p[j] == p[k]:
            if k == 0:
                fail[j] = 1
            else:
                fail[j] = fail[k-1] + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail

def KMP_Main():
    t = input("Enter the text: ")
    p = input("Enter the pattern: ")
    print("Pattern is at index: ", find_kmp(t,p))

KMP_Main()