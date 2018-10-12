def quicksort(array):
    l = len(array)
    pivot = array[l-1]
    
    i = 0
    j = len(array)
    while i < j:
        num = array[i]
        placeholder = array[j-2]  

        #print('i:',i, 'pivot:',pivot,'num:', num,'placeholder:',placeholder)
        
        if num > pivot:
            l = len(array)
            array[j-1] = num
            array[i] = placeholder
            array[j-2] = pivot
            
            print(array)
            i = i - 1
            j -= 1
    #        print(num)
        i += 1
    #return array[:i], array[i:]
    
    if len(array[:i]) > 1:
        array[:i-1] = quicksort(array[:i-1])
    if len(array[i:]) > 1:
        array[i:] = quicksort (array[i:])
    return array