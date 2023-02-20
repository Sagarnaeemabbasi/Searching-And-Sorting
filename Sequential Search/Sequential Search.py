pof = 0


def search(list, n):
    i = 0
    while i < len(list):
        globals()['pof'] = i
        if list[i] == n:
            return True
        i = i+1
    return False


list = [4, 5, 78, 65, 45, 76]
n = 76
if search(list, n):
    print("found at", pof+1)
else:
    print("not found")
