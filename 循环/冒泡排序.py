#
# array = [9,2,7,4,5,6,3,8,1,10]
# len = len(array)
# for i in range(len):
#     for j in range(len-i):
#         if array[i]>array[j+i]:
#             array[i],array[j+i] = array[j+i],array[i]
#
# for a in array:
#    print(a,end=" ")

array = [8, 2, 6, 3, 4, 5, 7, 1, 10, 9]
L = len(array)
for i in range(1, L):
    temp = array[i]
    array.remove(array[i])
    for j in range(i):
        if array[j] > temp:
            array.insert(j, temp)
            break
    else:
        array.insert(i, temp)
print(array)

def sample(n_samples):
    pass
