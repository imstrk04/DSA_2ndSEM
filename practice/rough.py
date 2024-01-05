def solution():
    area = int(input("Enter the area: "))
    l = []
    for num in range(1,area+1):
        if area % num == 0:
            l.append(num)
    l1 = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            prod = l[i] *l[j]
            if prod == area:
                l1.append((l[i],l[j]))
            if l[i] * l[i] == area:
                l1.append((l[i],l[i]))
    min_diff = 100000000000
    min_tup = None
    for tup in l1:
        diff = tup[1] - tup[0]
        if diff < min_diff:
            min_diff = diff
            min_tup = tup
    
    print("Minimum Length and Breadth are:",min_tup)

solution()