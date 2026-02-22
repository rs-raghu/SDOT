s = input().strip()
n = len(s)
found = False
for leng in range(n,0,-1):
    for start in range(n-leng+1):
        sub = s[start:start+leng]
        if sub == sub[::-1]:
            print(sub)
            found = True
            break
    if found:
        break