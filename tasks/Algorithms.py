def linearSearch(list, target):
    '''Returns the position of target value in the given list'''
    for i in range(len(list)):
        if list[i]==target:
            return i
    return None

def binarySearch(list,target):
    '''Returns the position of target value in the given sorted list'''
    first = 0
    last = len(list)-1
    while first<=last:
        mid=(first+last)//2
        if list[mid] == target:
            return mid
        elif list[mid]<target:
            first=mid+1
        else:
            last=mid-1
    return None

