from array import *
arr1 = array('i',[1,2,3,4,80,5])
for i in arr1:
    print(i)

# Access individual elements through indexes
print("Step 2")
print(arr1[3])

#append()

print("Step 3")
arr1.append(9)
print(arr1)

#insert()

print("Step 4")
arr1.insert(5, 80)
print(arr1)

#extend()
print("Step 5")
arr2 = array('i',[30,40,50])
arr1.extend(arr2)
print(arr1)

#fromlist()

print("Step 6")
list = [20,21,22]
arr1.fromlist(list)
print(arr1)

#remove()

print("Step 7")
arr1.remove(22)
print(arr1)

#pop()
print("Step 8")
arr1.pop()
print(arr1)

#find index()

print("step 9")
print(arr1.index(20))

#reverse()
print("step 10")
arr1.reverse()
print(arr1)

#buffer_info()
print("step 11")
print(arr1.buffer_info())


#count()
print("step 12")
print(arr1.count(80))

#slice
print("step 13")
print(arr1[11:])
