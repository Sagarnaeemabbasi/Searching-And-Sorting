def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            return True
        i=i+1
    return False
list=[2,4,63,9,54,34]
n=35
if search(list,n):
    print("found")
else:
    print("not found")