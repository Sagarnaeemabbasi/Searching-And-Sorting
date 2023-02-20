def search(list, n):
    first_term = 0
    last_term = len(list)-1
    while first_term <= last_term:
        mid_term = (last_term+first_term)//2
        if list[mid_term] == n:
            return True
        else:
            if list[mid_term] < n:
                first_term = mid_term+1
            else:
                last_term = mid_term-1
    return False


list = [2, 4, 6, 8, 9, 65]
n = 65
if search(list, n):
    print("found ")
else:
    print("not found")
