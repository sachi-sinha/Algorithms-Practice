
# Code useful for finding a single peak 

def peakFinder(array, low, high): 
    # low = starting index
    # high = last index in array
    
    # Calculating middle index of array
    mid = (low + high)/2
    mid = int(mid)
    
    # if the number on left is greater, search in left half
    if mid > 0 and array[mid - 1] > array[mid]:
        return peakFinder(array, low, mid -1)
        
    # if number on right is greater, search in right half
    elif mid > 0 and array[mid + 1] > array[mid]:
        return peakFinder(array, mid + 1, high)
    
    # if number is the only element or middle number is the peak itself
    else:
        return array[mid]

print(peakFinder([6, 7, 4, 3, 2, 1, 4], 0, 7))
   
