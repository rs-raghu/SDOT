def find_it(s):
    rev = s[::-1]
    if(s==rev):
        return s
    else:
        return rev[:-1]+s
s = input()
a = find_it(s)
print(a)