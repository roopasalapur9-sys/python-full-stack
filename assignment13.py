scores=[45,30,35,12,10]
total=0
for s in scores:
    total=total+s
average=total/len(scores)
count=0
for s in scores:
    if s>average:
        count=count+1
print("scores:",scores)
print("total scores:",total)
print("average score;",average)
print("count of scores above average:",count)
