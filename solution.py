p=open("path.txt").read()
m,i,b,c=0,0,-1,0
for x in p:
 if x=="U":c+=1
 else:
  if c>m:m=c;b=i-c
  c=0
 i+=1
if c>m:b=i-c
print(b)
