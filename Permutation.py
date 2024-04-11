def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 ==  list2:
        return True
    else:
        return False
li1= [1,2,4,5]
li2=[4,5,2,1]
print(permutation(li1,li2))