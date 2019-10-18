list = [1,2,3,4,5,6,7,8,9,10]
print(list)
list_tmp = list[5:10]
list2=list_tmp
list=list[0:5]
print(list)
print(list2)
list = list + list2
list.reverse()
list.append(0)
list.reverse()
list.sort(reverse=True)
print(list)

