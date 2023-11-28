def quicksort(array):
    if len(array)<2:
        return array #基线条件
    else:
        pivot =array[0] #递归条件，基准值
        less =[i for i in array[1:] if i<=pivot]#所有小于基准值的元素
        greater=[i for i in array[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
    
print(quicksort([10,3,5,5,6]))
