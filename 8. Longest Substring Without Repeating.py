s = input()
n = len(s)
sett = set()
left = 0
max_l=0
for right in range(n):
    while s[right] in sett:
        sett.remove(s[left])
        left = left+1
    sett.add(s[right])
    max_l = max(max_l,right-left+1)

print(max_l)