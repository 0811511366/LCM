def LCM(x, b):
    greater = max(x, b)
    smallest = min(x, b)
    for i in range(greater, x*b+1, greater):
        if i % smallest == 0:
            return i

# Driver program to test above function
if __name__ == '__main__':
    x = 25
    b = 350
    print("LCM of", x, "and", b, "is", LCM(x, b))