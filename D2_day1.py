#Update file on 10 May 2025
list1 = [5, 1, 8, 9, 4, 3]
for i in range(len(list1)-1):
    if list1[i] > list1[i+1]:
        list1[i], list1[i+1] = list1[i+1], list1[i]
        print(list1)