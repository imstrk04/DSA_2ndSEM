import random
from timeit import default_timer as timer

def createList():
    n = int(input("Enter number of elements: "))
    seq = []
    for i in range(n):
        seq.append(random.randint(0,1000))
    print("Original List:", seq)
    return seq

def bubbleSort(seq):
    n = len(seq)
    fn = 0
    swap = 0
    start = timer()
    for i in range(n-1):
        fn += 1
        for j in range(n - i - 1):
            fn += 1
            if seq[j] > seq[j+1]:
                swap += 1
                seq[j], seq[j+1] = seq[j+1], seq[j]
    end = timer()
    print("F(n):", fn)
    print("No of comparisons:", swap)
    print("Total time:",end - start)
    return seq

#print("Sorted List:", bubbleSort(createList()))

def selectionSort(seq):
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    for i in range(n-1):
        fn += 1
        minIndex = i
        for j in range(i+1, n):
            fn += 1
            if seq[minIndex] > seq[j]:
                swap += 1
                minIndex = j
        seq[i], seq[minIndex] = seq[minIndex], seq[i]
    end = timer()
    print("F(n):", fn)
    print("No of comparisons:", swap)
    print("Total time:",end - start)   
    return seq

#print("Sorted List:", selectionSort(createList()))

def InsertionSort(seq):
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    for i in range(1,n):
        fn += 1
        temp = seq[i]
        j = i - 1
        while (j >= 0 and seq[j] > temp):
            fn += 1
            seq[j+1] = seq[j]
            j = j - 1
            swap += 1
        seq[j+1] = temp
    end = timer()
    print("F(n):", fn)
    print("No of comparisons:", swap)
    print("Total time:",end - start)
    return seq

#print("Sorted List:", InsertionSort(createList()))


def Merge(a, b, fn, swap):
    c = []
    m = len(a)
    n = len(b)
    i = j = 0
    while i < m and j < n:
        fn += 1
        if b[j] < a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
            swap += 1
    
    while i < m:
        c.append(a[i])
        i += 1

    while j < n:
        c.append(b[j])
        j += 1
    
    return c, fn, swap

def MergeSort(seq, fn = 0, swap = 0):
    n = len(seq)
    if n < 2:
        return seq, fn, swap
    else:
        mid = n // 2
        left,fn,swap = MergeSort(seq[:mid], fn, swap)
        right,fn,swap = MergeSort(seq[mid:], fn, swap)
        merged_seq, fn, swap = Merge(left,right,fn, swap)
        return merged_seq, fn, swap

def EmpiricalAnalysisMergeSort(seq):
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    sorted_seq, fn, swap = MergeSort(seq, fn, swap)
    end = timer()
    print("Sorted sequence:", sorted_seq)
    print("F(n):", fn)
    print("No of comparisons:", swap)
    print("Total time:", end - start)
    return sorted_seq

# Example usage:
seq = [4, 1, 7, 3, 8, 5, 2, 6]
print("Original sequence:", seq)

EmpiricalAnalysisMergeSort(seq)

def median(L):
    n = len(L)
    low, mid,high = L[0], L[n//2], L[n-1]
    if low>high:
        L[0], L[n-1] = L[n-1], L[0]
    if high > mid:
        L[n-1], L[n//2] = L[n//2], L[n-1]
    if low > mid:
        L[0], L[n // 2] = L[n // 2], L[0]
    return L

def partition(L,begin,end):
    fn = 0
    swap = 0
    pivot = L[end]
    i, j = begin, end -1
    while (i <=j):
        while(L[i] <= pivot and i < end):
            fn += 1
            i += 1
        while (L[j] > pivot and j >= begin):
            fn += 1
            j -= 1
        if i < j:
            swap += 1
            L[i], L[j] = L[j], L[i]
    L[i], L[end] = L[end], L[i]
    return i, L[i:i+1], fn, swap

def quick_sort(L):
    if len(L) < 2:
        return L, 0, 0
    else:
        L = median(L)
        position, mid, fn1, swap1 = partition(L,0,len(L)-1)
        lhs, fn2, swap2 = quick_sort(L[:position])
        rhs, fn3, swap3 = quick_sort(L[position + 1:])
        return lhs + mid + rhs, fn1 + fn2 + fn3, swap1 + swap2 + swap3

'''start = timer()
list, fn, swap = quick_sort(createList())
print("Sorted List: ")
print(list)
print("Total Comparisons:", fn)
print("Total Swapings:", swap)
end = timer()
print("The time taken is", end - start)'''
