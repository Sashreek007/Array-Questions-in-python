import numpy as np

def average_temp():
    a = int(input("How many days temperature do you want?"))
    temperatures=np.array([])
    for i in range(1,a+1):
        b=int(input("Day"+str(i)+"'s temperature?"))
        temperatures= np.append(temperatures,b)
    average = np.average(temperatures)
    print("Average:",average)
    average_count=0
    for i in range(len(temperatures)):
        if temperatures[i]> average:
            average_count+=1
    print(average_count,"Days(s) above temperature")       
average_temp()
