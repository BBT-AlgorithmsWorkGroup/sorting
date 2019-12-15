def sort(list1):
    sortedlist=[]    
    def min(list1):
        mini=list1[0]
        for i in list1:
            if i<mini:
                mini=i
        return mini
    for a in range(len(list1)):
        sortedlist.append(min(list1))
        list1.pop(list1.index(min(list1)))
    return sortedlist

n=int(input("how many numbers==>"))
numlist=[]
output=""
for i in range(n):
    num=int(input("enter number==>"))
    numlist.append(num)
a=sort(numlist)
i=0
while i<len(a):
    output+=str(a[i])
    output+="-"
    i+=1
output=output[:-1]
print(output)
        
    
