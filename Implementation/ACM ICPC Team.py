n,m=map(int,input().split())
person=list()
for i in range(n):
    person.append(int(input(),2))
result=list()
for i in range(n-1):
    for j in range(i+1,n):
        result.append(format(person[i]|person[j], 'b'))
person=[]
for i in result:
    person.append(i.count('1'))
print(max(person))
print(person.count(max(person)))
