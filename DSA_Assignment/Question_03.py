l = [1,2,4,3,2,4,2,5,7,2]
print ("Given List : " + str(l))
max = 0
res = l[0]
for i in l:
    freq = l.count(i)
    if freq > max:
        max = freq
        res = i
print ("Frequent Number : " + str(res))