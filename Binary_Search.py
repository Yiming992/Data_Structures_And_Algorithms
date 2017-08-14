"""
Binary Search of an ordered list

"""




def binarySearch(alist,item):

    first=0
    last=len(alist)-1
    found=False

    while first<=last and not found:
        mid=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if item<alist[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found
