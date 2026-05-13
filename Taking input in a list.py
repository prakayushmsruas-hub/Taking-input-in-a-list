print("Taking input in a list\n")
lst=[]           #taking an empty list so that we append elements later
n=int(input("enter number of elements you want in the list:"))
for i in range(0,n):
    elements=input("Enter elements:")
    lst.append(elements)           #appending
print(lst)
