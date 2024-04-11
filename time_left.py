tickets = [2,3,2]
k=2
tickets = [5,1,1,1]
k = 0
def time(tickets,k):
    time=0
    while tickets[k]>0:
        for i in range(len(tickets)):
            if tickets[i]>0:
                tickets[i]-=1
                time+=1
                if  i==k and tickets[i]==0:
                    break
    return time
    
print(time(tickets,k))