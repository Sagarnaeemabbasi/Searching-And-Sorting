pof=0
def search(list,n):
    for i in range (len(list)):
        globals()['pof']=i+1
        if list[i]==n:
            return True
        i=i+1
    return False
list=[4,5,78,65,45,7,876]
n=8
if search(list,n):
    print("found at",pof)
else:
    print("not found")