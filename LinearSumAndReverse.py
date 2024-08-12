def reverse(s, start, stop):
    if start< stop-1:
        s[start], s[stop-1] = s[stop-1], s[start]
        reverse(s, start+1, stop-1)

def LinearSum(s, n):
    if n == 1:
        return s[0]
    else:
        return LinearSum(s,n-1)+s[n-1]
    
def runLinearSum():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = LinearSum(data, len(data))
    print(sum)

def runReverse():
    s = list("hello")
    reverse(s, 0, len(s))
    print("".join(s))

runLinearSum()
runReverse()
