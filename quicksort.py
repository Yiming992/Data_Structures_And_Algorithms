def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[]
        greater=[]
        for i in array[1:]:
            if i<=pivot:
                less.append(i)
            elif i>pivot:
                greater.append(i)
        return quicksort(less)+[pivot]+quicksort(greater)

if __name__=='__main__':

    test_array=[10,7,8,9,1,5,15,3,2,19,20]
    print(quicksort(test_array))