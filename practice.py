import array
import numpy as np

arr1= [1,2,3,4,6]

def missing_number(array):
    n= len(array)+1
    sum = n*(n+1)/2
    element_sum=0
    for i in range(len(array)):
        element_sum += array[i]
    number = sum - element_sum
    return number
print(missing_number(arr1))

def Two_sum(array,target):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]== target:
                return (array[i],array[j])
print(Two_sum(arr1,9))