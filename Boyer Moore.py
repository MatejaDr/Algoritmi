def find_Boyer_Moore(t, p):
    n, m = len(t), len(p)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[p[k]] = k
    i = m - 1
    k = m - 1
    while i < n:
        if t[i] == p[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(t[i], -1)
            i += m - min(k,j+1)
            k = m - 1
    return NoMatchException("There is no match.")

class NoMatchException(Exception):
    pass

def BoyerMooreMain():
    t = input("Enter the text: ")
    p = input("Enter the pattern: ")
    print("Pattern is at index: ", find_Boyer_Moore(t, p))

BoyerMooreMain()