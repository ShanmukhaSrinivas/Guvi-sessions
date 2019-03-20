def recur(s,i):
   if l//2>i:
       s[i],s[l-i-1]=s[l-i-1],s[i]
       recur(s,i+1)


s = list(input())
l = len(s)
recur(s,0)
print(s)
