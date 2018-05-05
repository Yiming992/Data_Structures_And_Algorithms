

def merge(a,b):
    pointer1=0
    pointer2=0
    merged=[]
    status=True
    while status:
        if a[pointer1]<b[pointer2]:
            merged.append(a[pointer1])
            pointer1+=1
        else:
            merged.append(b[pointer2])
            pointer2+=1
        if pointer1>=len(a):
            merged.extend(b[pointer2:])
            status=False
        elif pointer2>=len(b):
            merged.extend(a[pointer1:])
            status=False
    return merged
            
    
def mergeSort(a):
    if len(a)==1:
        return [a[0]]
    else:
        return merge(mergeSort(a[:len(a)//2]),mergeSort(a[len(a)//2:]))


if __name__=='__main__':

    sample=[38,27,43,3,9,82,10]
    print(mergeSort(sample))


