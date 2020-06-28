def getPivot(array, l, h):
    pivot = array[h]
    i = l
    for j in range(l, h):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[h] = array[i]
    array[i] = pivot
    return i
    
def quicksortHelper(array, low, high):
    
    if low < high:
            p = getPivot(array, low, high)
            quicksortHelper(array, low, p - 1)
            quicksortHelper(array, p + 1, high)
            
def quicksort(alist):

  quicksortHelper(alist,0,len(alist)-1)
  return alist

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
