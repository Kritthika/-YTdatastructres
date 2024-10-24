def max_product(arr):  
    max1, max2 = 0 , 0
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 =i 
    result = max1 * max2 
    return result
arr = [1, 7, 3, 4, 9, 5,10] 
print(max_product(arr))