list1=[]  
list2=[]  
num1=int(input("Enter number of elements for first list:"))  
for i in range(1,num1+1):  
    b=int(input("Enter element:"))  
    list1.append(b)  
  
num2=int(input("Enter number of elements for second list:"))  
for i in range(1,num2+1):  
    d=int(input("Enter element:"))  
    list2.append(d)  
  
for i in range(len(list1)-1):  
    for j in range(len(list2)- 1):  
        if list1[i]>list2[j] and list1[i] < list2 [j+1]:  
            list2.insert(j+1, list1[i])  
print("Sorted list is:", list2) 

