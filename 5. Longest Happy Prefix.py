s = input()
max = 0
for i in range(1,len(s)):
    if s[:i] == s[len(s)-i:]:
        max = i

print(s[:max])