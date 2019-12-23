import random

def minimum(l):
    min = l[0]
    for i in l:
        if min > i:
            min = i
    return min
    
def mysort(lm):
    lm = lm[:]
    newlist = []
    while len(lm) > 0:
        m = minimum(lm)
        newlist.append(m)
        lm.remove(m)
    return newlist
#insert
def in_sort(n, nlist):
    inds = 0
    while inds < len(nlist) and n > nlist[inds]:
        inds +=1
    nlist.insert(inds, n)


def av_sort(arr):
    if len(arr) <= 1:
        return arr    
    av = sum(arr)/len(arr)
    more = []
    less = []
    av_arr = []
    for i in arr:
        if i < av:
            less.append(i)
        elif i == av:
            av_arr.append(i)
        else:
            more.append(i)
    return av_sort(less)+av_arr+av_sort(more)

nlist = []

t= int(input(" ? "))
for i in range(t):
    in_sort(int(input()),nlist)

#Test
#for i in range(random.randrange(10, 2000)):
#        in_sort(random.randrange(0, 2000),nlist)
print(nlist)
print(nlist == sorted(nlist))    

