#Separating -ve and +ve numbers in a list to left and right side

'''def seperate(arr):
    low = 0
    high = len(arr) - 1
    while (low < high):
        if arr[low] < 0:
            low += 1
        elif arr[high] > 0:
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
    return arr

print(seperate([1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]))'''

#Output [-9, -8, -4, -5, -6, -7, 3, 2, 2, 2, 1, 3, 2, 1] Order doesnt matter.

#Cycically rotate an array
'''def rotate( arr, n):
    
    last_ele = arr[n-1]
    
    for i in range(n-1, 0, -1):
        print(f"{i} iteration list:", arr)
        arr[i] = arr[i-1]
    
    arr[0] = last_ele
    
    return arr

print(rotate([1,2,3,4,5], 5))'''

#Maximum sum of subarray, KADANE's Algorithm

'''def Kadanes(arr):
    maxSum = arr[0]
    curSum = 0

    for num in arr:
        curSum = max(curSum, 0)
        curSum += num
        maxSum = max(maxSum, curSum)

    return maxSum

def SlidingWindow(arr):
    maxSum = arr[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(arr)):
        if curSum < 0:
            curSum = 0
            L = R
        curSum += arr[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R
    
    return [maxL, maxR]

print("Maximum sum of subarray:", Kadanes([-2, -3, 4, -1, -2, 1, 5, -3]))
print("Left Index and Right Index:", SlidingWindow([-2, -3, 4, -1, -2, 1, 5, -3]))'''

'''def subArraySum(arr, n, s): 
    #Write your code here
    currsum = arr[0]
    #L = 0
    #finalL, finalR = 0, 0
    for num in arr:
        currsum += num
        if currsum == s:
            return True
        

    return [-1]

print(subArraySum([1,2,3,7,5], 5, 12))'''

'''t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    Sum = 0
    if n == 2:
        print("Yes")
    else:
        for i in range(n):
            Sum += arr[i]
        if Sum % 2 == 0:
            print("Yes")
        else:
            print("No")
    
    
    t -= 1'''
'''
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = []
    xor = 0
    for i in range(8):
        if all(x == 0 for all x in arr):
            break
        
        for j in range(n):
            if a[j] != 0:
                l = j
                break
            
        for r in range(n-1, -1, -1):
            if a[j] != 0:
                r = j
                break
        xor = 0
        for j in range(l, r+1):
            xor = xor ^ a[j]
        
        for j in range(l, r+1):
            a[j] = xor
        
        k.append((l+1, r+1))
    operations = len(k)
    print(operations)
    for l in k:
        print(l[0], l[1])
        
'''
'''t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    is_good = True
    Sum = arr[0] + arr[1]
    if n <= 2:
        is_good = True
    if n == 3:
        xor = 0
        for i in range(len(arr)):
            xor = xor ^ arr[i]
        if xor != 0:
            is_good = True
        if xor == arr[0] or xor == arr[1] or xor == arr[2]:
            is_good = True
    for j in range(len(arr)-1):
        if arr[j] + arr[j+1] != Sum:
            is_good = False
    if is_good:
        print("Yes")
    else:
        print("No")'''
'''t = int(input()) 

for _ in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))

    is_good = False  
    Sum = arr[0] + arr[1]

    if n <= 2:
        is_good = True 
    elif n == 3:
        xor = 0
        for i in range(len(arr)):
            xor = xor ^ arr[i]  
        if xor == 0 or Sum == arr[0] or Sum == arr[1] or Sum == arr[2]:
            is_good = True 

    if is_good:
        print("Yes")
    else:
        print("No")'''

'''t = int(input()) 

for _ in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))  

    is_good = False  
    Sum = arr[0] + arr[1]

    if n <= 2:
        is_good = True  
    elif n == 3:
        
        if (arr[0] == Sum or arr[1] == Sum or arr[2] == Sum):
            is_good = True
    else:

        for j in range(len(arr) - 1):
            if arr[j] + arr[j + 1] != Sum:
                is_good = False
                break
        else:
            is_good = True

    if is_good:
        print("Yes")
    else:
        print("No")
'''


'''
#339A Helpful Maths
s  = input()
lst = s.split("+")
lst.sort()
final = ""
for i in range(len(lst)- 1):
    final = final + lst[i] + "+"
final += lst[-1]
print(final)'''

'''
50A - Domino Piling
m, n = map(int, input().split())
area = m * n
k = area // 2
print(k)
'''

'''
71A - Way too Long Words
n = int(input())
for _ in range(n):
    s = input()
    final = ""
    if len(s) > 10:
        count = 0
        final += s[0]
        for i in range(1,len(s)-1):
            count += 1
        final += str(count) + s[-1]
        print(final)
    else:
        print(s)'''

'''
282A Bit++
n = int(input())
count = 0
for _ in range(n):
    s = input()
    if s[0] == '+' or s[-1] == '+':
        count += 1
    elif s[0] == '-' or s[-1] == '-':
        count -= 1
print(count)'''

'''
281A Word Capitalisation
s = input()
final = ""
if not s[0].isupper():
    final += s[0].upper()
    for i in range(1, len(s)):
        final += s[i]
    print(final)
else:
    print(s)'''

'''
236A Boy or Girl
s = input()
count = 0
lst = []
for ch in s:
    if ch in lst:
        count += 1
    lst.append(ch)
ans = len(s) - count
if ans % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")'''


'''#118A - String Task
s = input()
final = ""
for ch in s:
    if ch.lower() in "aeiouy":
        continue
    else:
        final = final + "." + ch.lower()
print(final)'''

'''
266A - Stones on the Table
n = int(input())
s = input()
count = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
print(count)'''


'''
791A - Bear and the Brother
a, b = map(int, input().split())
count = 0
while a <= b:
    a = a * 3
    b = b * 2
    count += 1
print(count)'''

'''
#617A - Elephant
x2 = int(input())
count = 0
while x2 > 0:
    if x2 >= 5:
        x2 -= 5
        count += 1
    elif 4 <= x2 < 5:
        x2 -= 4
        count += 1
    elif 3 <= x2 < 4:
        x2 -= 4
        count += 1
    elif 2 <= x2 < 3:
        x2 -= 4
        count += 1
    elif 4 <= x2 < 5:
        x2 -= 4
        count += 1
print(count)'''

'''
#546A - Soldier and Bananas
k, n, w = map(int, input().split())
cost = 0
for i in range(1, w+1):
    cost = cost + k * i
if cost > n:
    ans = cost - n
    print(ans)
else:
    print(0)'''

'''
59A - Word
s = input()
lower, upper = 0, 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

if upper > lower:
    print(s.upper())
else:
    print(s.lower())'''

'''def poly(L, x_0):
    psum = 0
    n = len(L)
    for i in range(n):
        psum = psum + L[i] * (x_0 ** i)
    return psum

def poly_zeros(L, a, b):
    zeros = [ ]
    for x in range(a, b + 1):
        if poly(L, x) == 0:
            zeros.append(x)
    return zeros

print(poly_zeros([2,-3,1],0,4))'''

'''def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print("Nums:", nums)
        num_index = {}
        for i in range(len(nums)):
            num = nums[i]
            num_index[num] = i
        
        num_index_sorted = dict(sorted(num_index.items()))
        print("Sorted dict", num_index_sorted)

        left, right = 0, len(nums) - 1

        while left <= right:
            print("left index:", left)
            print("right index:", right)
            left_num = nums[left]
            print("Left num:", left_num)
            right_num = nums[right]
            print("Right Num", right_num)
            Sum = left_num + right_num
            print("SUM:", Sum)
            if Sum == target:
                return [num_index_sorted[left_num], num_index_sorted[right_num]]
            elif Sum < target:
                left += 1
            elif Sum > target:
                right -= 1
'''

'''def twoSum(nums, target):
    num_index = {}
    for i, num in enumerate(nums):
        if target - num in num_index:
            return [num_index[target - num], i]
        num_index[num] = i
    for i in range(len(nums)):
        num = nums[i]
        num_index[num] = i
    
    num_index_sorted = dict(sorted(num_index.items()))

    left, right = 0, len(nums) - 1

    while left < right:
        left_num = nums[left]
        right_num = nums[right]
        Sum = left_num + right_num

        if Sum == target:
            return [num_index_sorted[left_num], num_index_sorted[right_num]]
        elif Sum < target:
            left += 1
        elif Sum > target:
            right -= 1

    return None

print("Indices are:",twoSum([3,2,4], 6))'''


'''
977A - Wrong Subtraction
n, k = map(int, input().split())

for _ in range(k):
    last_dig = n % 10
    if last_dig == 0:
        n = n // 10
    elif last_dig != 0:
        n = n - 1
print(n)
'''

'''
96A - Football
s = input()
if "0000000" in s or "1111111" in s:
    print("YES")
else:
    print("NO")
'''
'''
n = input()

lucky = 0

for i in range(len(n)):
    if n[i] == '4' or n[i] == '7':
        lucky += 1
if lucky == 4 or lucky == 7 or lucky == len(n):
    print("YES")
else:
    print("NO")'''

'''def buildarray(target, n):
    s = []
    i = 0
    for num in target:
        while i < num - 1:
            s.append("Push")
            s.append("Pop")
            i += 1
        s.append("Push")
        i += 1
    print(s)

buildarray([1,2], 4)'''

'''def majorityelement(arr):
    hashmap = {}
    n = len(arr)
    reqd = n // 2
    for num in arr:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    for count in hashmap.values():
        if count > reqd:
            print(count)
    return -1


majorityelement([2,2,3,3,1,2,2])'''

'''def majorityelement(arr):
    count = 0
    for i in range(len(arr)):
        if count == 0:
            count = 1
            el = arr[i]
        elif arr[i] == el:
            count += 1
        else:
            count -= 1
    count1 = 0
    for i in range(len(arr)):
        if arr[i] == el:
            count1 += 1
    
    if count1 > len(arr) // 2:
        print(el)
    else:
        print(-1)

majorityelement([3,3,4])'''

'''def maxSubArray(nums):
    maxi = -10000000000000000
    Sum = 0
    ansStart, ansEnd = -1, -1
    for i in range(len(nums)):
        if Sum == 0: start = i
        Sum += nums[i]
        if Sum > maxi:
            maxi = Sum
            ansStart = start
            ansEnd = i
        if Sum < 0:
            Sum = 0 
    
    print("Maximum Sum:",maxi)
    print("Subarray:", end = " ")
    for i in range(ansStart, ansEnd+1):
        print(nums[i], end = " ")

maxSubArray([-2,-3,4,-1,-2,1,5,-3])'''

'''n = int(input())
s = input()
countA = 0
countD = 0
for i in range(n):
    if s[i] == "A":
        countA += 1
    if s[i] == "D":
        countD += 1

if countA > countD:
    print("Anton")
elif countA < countD:
    print("Danik")
elif countA == countD:
    print("Friendship")'''

'''s = input()
t = input()
l1 = list(s)
l2 = list(t)
l3 = l2[::-1]
if l3 == l1:
    print("Yes")
else:
    print("No")'''

'''def getWinner(arr,k):
    n = len(arr)
    hashmap = {}
    for i in range(n):
        hashmap[arr[i]] = 0
    while k>0:
        if arr[0] > arr[1]:
            hashmap[arr[0]] += 1
            print("arr[0]:",arr[0],hashmap[arr[0]])
            rotate1(arr)
        elif arr[0] < arr[1]:
            hashmap[arr[1]] += 1
            print("arr[1]:",arr[1],hashmap[arr[1]])
            rotate2(arr)
        
    print(hashmap)


def rotate1(arr):
    temp = arr[1]
    for i in range(1, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = temp

def rotate2(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp'''

'''def getWinner(arr, k):
    n = len(arr)
    consecutive_wins = 0
    current_winner = arr[0]

    while consecutive_wins < k:
        if arr[0] > arr[1]:
            consecutive_wins += 1
            rotate1(arr)
            current_winner = max(current_winner, arr[0])
        else:
            consecutive_wins = 1
            rotate2(arr)
            current_winner = arr[0]

    return current_winner

def rotate1(arr):
    arr.append(arr.pop(1))

def rotate2(arr):
    arr.append(arr.pop(0))


print(getWinner([2,1,3,5,4,6,7], k = 2))'''

'''def rearrange(arr):
    n = len(arr)
    ans = [0 for i in range(n)]
    pos = 0
    neg = 1
    for i in range(n):
        if arr[i] < 0:
            ans[neg] = arr[i]
            neg += 2
        else:
            ans[pos] = arr[i]
            pos += 2
    print(ans)


rearrange([3,1,-2,-5,2,-4])'''

'''n = int(input())
Sum = 0
maxi = 0
for i in range(n): 
    a, b = list(map(int, input().split()))
    Sum = Sum - a + b
    maxi = max(Sum, maxi)
print(maxi)'''

'''n, h = map(int, input().split())
a = list(map(int, input().split()))
width = 0

for ht in a:
    if ht <= h:
        width += 1
    else:
        width += 2

print(width)'''

'''n, t = map(int, input().split())
s = input()
lst = list(s)

for _ in range(t):
    i = 0
    while i < n - 1:
        if lst[i] == 'B' and lst[i+1] == 'G':
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 2
        else:
            i += 1
final = ""
for ch in lst:
    final += ch
print(final)'''

'''y = int(input())

while True:
    y += 1
    if len(set(str(y))) == 4:
        print(y)
        break'''

'''s = input()
lst = []

for i in range(len(s)):
    if s[i] not in "hello":
        continue
    else:
        lst.append(s[i])
print(lst)'''

'''n = int(input())
hashmap = {}
output = []
for _ in range(n):
    s = input()
    if s not in hashmap:
        hashmap[s] = 1
        output.append("OK")
    else:
        while s + str(hashmap[s]) in hashmap:
            hashmap[s] += 1
        new = s + str(hashmap[s])
        hashmap[new] = 1
        output.append(new)

for words in output:
    print(words)'''


'''
def topKFrequent( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hashmap = {}
    output = []
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
    print(hashmap)
    hm_sorted = sorted(hashmap.values(), reverse = True)[k-1]
    print(hm_sorted)
    for i in hashmap:
        print(hashmap[i])
        if hashmap[i] < hm_sorted:
            continue
        else:
            output.append(i)

    print(output)

topKFrequent([1,1,1,2,2,3], 2)'''

'''lst = [1,5,6,2]
lst.sort()
l = []
popp = lst.pop(0)
l.append(popp)
print(l)'''

'''s = input()
msg = ""

for ch in s:
    while True:
        if ch in "hello":
            msg += ch
        

if msg == "hello":
    print("YES")
else:
    print("NO")'''

'''def solution(n, l):
    for n in l:
        if n == 1:
            return "HARD"
    return "EASY"

n = int(input())
l = list(map(int, input().split()))
print(solution(n, l))'''


'''n = int(input())

s = str(n)
print(s)
isLucky = False

lst = list(s)
print(lst)
for num in lst:
    if num == '4' and num == '7':
        isLucky = True

if isLucky:
    print("YES")
else:
    print("NO")'''

'''n = int(input())
count = 0
for _ in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:
        count += 1

print(count)'''

'''
160A - Twins
n = int(input())
a = list(map(int, input().split()))
count = 1

a.sort()
a = a[::-1]

twin1 = a[0]

twin2 = sum(a) - twin1


for i in range(1,len(a)):
    if twin1 <= twin2:
        twin1 += a[i]
        count += 1
        twin2 = twin2 - a[i]
print(count)'''

'''def solution(n):
    l = []
    for i in range(n):
        l.append(int(input()))

    group = 0
    maxm = 0
    if len(l) < 2:
        return 1
    elif len(l) == 2:
        return 2
    else:
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                group += 1
                maxm = max(group, maxm)

        return maxm

n = int(input())
print(solution(n))'''


'''def restoreArray(adjacentPairs):
    """
    :type adjacentPairs: List[List[int]]
    :rtype: List[int]
    """
    hashmap = {}
    for i in adjacentPairs:
        for j in i:
            if j in hashmap:
                hashmap[j] += 1
            else:
                hashmap[j] = 1
    l = []
    
    for key, val in hashmap.items():
        if val <= 2:
            l.append(key)
    
    return l'''

'''def func(n):
    if n % 2 != 0:
        ans = (-1) * ((n+1)//2)
    else:
        ans = n // 2
    print(ans)

n = int(input())
func(n)
        '''

'''p = input()
isJoke = False
for ch in p:
    if ch == 'H' or ch == 'Q' or ch == 9 or ch == '+':
        isJoke = True
        break

if isJoke:
    print("YES")
else:
    print("NO")'''

'''n, k = map(int, input().split())
l = []
for i in range(n):
    l.append(i+1)
even = []
odds = []
for i in range(1,len(l)+1):
    if i % 2 == 0:
        even.append(i)
    else:
        odds.append(i)
new = []
new.extend(odds)
new.extend(even)
print(new[k-1])'''

'''n1 = input()
n2 = input()
n3 = ""

for i in range(len(n1)):
    if n1[i] != n2[i]:
        n3 += '1'
    else:
        n3 += '0'

print(n3)'''

'''n = int(input())
a = list(map(int, input().split()))

hashmap = {}

for i in range(len(a)):
    hashmap[a[i]] = i+1
sorted_hashmap = dict(sorted(hashmap.items()))
for key, val in sorted_hashmap.items():
    print(val, end = " ")'''

'''a = list(map(int, input().split()))
maxi = a[-1]
l = [maxi]
for i in range(len(a) - 1, -1, -1):
    if a[i] > maxi:
        l.append(a[i])
        maxi = max(a[i], maxi)

print(l)'''

'''n = int(input())
p = list(map(int, input().split()))
Sum = 0
for num in p:
    Sum += num
print(Sum/n)'''

'''s = list(map(int,input().split()))
l = []
to_buy = 0
for i in range(len(s)):
    if s[i] not in l:
        l.append(s[i])
    else:
        to_buy += 1

print(to_buy)'''

'''n = int(input())

feelings = ""
for i in range(1, n + 1):
    if i % 2 == 1:
        feelings += "I hate"
    else:
        feelings += "I love"
    
    if i != n:
        feelings += " that "

feelings += " it"

print(feelings)'''

'''def sortVowels(s):
    vowels = []
    for ch in s:
        if ch in "AaEeIiOoUu":
            vowels.append(ch)
    sorted_vowels = sorted(vowels)
    ans = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            ans += s[i]
        else:
            ans += sorted_vowels.pop(0)
    
    print(ans)

sortVowels("lEetcOde")'''

'''n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

p = a1[1:]
q = a2[1:]

final = []

for i in range(len(p)):
    final.append(p[i])

for i in range(len(q)):
    if q[i] not in final:
        final.append(q[i])

if len(final) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")'''

'''n = int(input())
a = list(map(int, input().split()))

a1 = sorted(a)
for num in a1:
    print(num, end = " ")'''

'''def countPalindromicSubsequence(s):
    n = len(s)
    letters = set(s)
    print(letters)
    count = 0
    maxm = 0
    hashmap = {}
    for i in range(n):
        if s[i] not in hashmap:
            hashmap[s[i]] = 1
        else:
            hashmap[s[i]] += 1
    if len(hashmap) == 1:
        return 1
    else:
        for key, val in hashmap.items():
            if val >=2 and val != count:
                count = val
                maxm = max(count, maxm)
            else:
                count = 2 * val
                maxm = max(count, maxm)
    return maxm

print(countPalindromicSubsequence("ckafnafqo"))'''

'''def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True'''

'''def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return [numbers[left], numbers[right]]
    
print(twoSum([-1,0], -1))'''

'''t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    count = 0
    ans = a % b

print(ans)'''

'''def long_tail(L):
    count1 = 0
    count2 = 0
    final = 0
    for floats in L:
        num = str(floats)
        print(num)
        index = 0
        for i in range(len(num)):
            if num[i] == '.':
                break
            else:
                index += 1
        first_half = num[:i+1]
        print(f"{num}'s first half:", first_half)
        second_half = num[i+1:]
        print(f"{num}'s second_half:", second_half)
        count1 = len(first_half)  
        print(f"{num}'s first half len:", count1)
        count2 = len(second_half)
        print(f"{num}'s second halg len:", count2)
        print("\n")
        if count2 > count1:
            final += 1
    print(final)

long_tail([12.1234, 155.231, 1981.1843213, 233.3333, 1001.1001, 100.0])'''

'''name, s1, s2 = map(str, input().split())
print(name)
print(s1)
print(s2)'''

'''t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a % b != 0:
        ans = b - (a % b)
    else:
        ans = 0
    print(ans)'''


'''s = input()
ans = ""
i = 0
while i < len(s):
    if s[i] == ".":
        ans += "0"
        i += 1
    elif s[i:i+2] == "-.":
        ans += "1"
        i += 2
    elif s[i:i+2] == "--":
        ans += "2"
        i += 2

print(ans)'''

'''a = int(input())
b = int(input())
c = int(input())

result1 = a + b + c
result2 = a * b * c
result3 = a + b * c
result4 = a * (b + c)
result5 = (a + b) * c
result6 = a * b + c


max_result = max(result1, result2, result3, result4, result5, result6)

print(max_result)'''

'''def minPairSum(nums):
    n = len(nums)
    nums.sort()
    i, j = 0, len(nums) - 1
    pairSum = []
    cnt = 0
    while cnt != n:
        Sum = nums[i] + nums[j]
        print(f"{nums[i]} + {nums[j]}:",Sum)
        pairSum.append(Sum)
        print("list:",pairSum)
        i += 1
        j -= 1
        cnt += 1

    ans = max(pairSum)
    return ans

print(minPairSum([3,5,4,2,4,6]))'''

'''def maxFrequency(nums, k):
    nums.sort()
    n = len(nums)
    hashmap = {}
    for i in range(n):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = 1
        else:
            hashmap[nums[i]] += 1
    count = 0
    for i in range(n):
        new = nums[i] + k
        if new in hashmap:
            hashmap[new] += 1
        else:
            new = nums[i] 

    print(hashmap)

maxFrequency([3,6,9], 2)
'''

'''def is_pangram(n, s):
    char_set = set()

    for char in s:
        if 'a' <= char.lower() <= 'z':
            char_set.add(char.lower())

    if len(char_set) == 26:
        return "YES"
    else:
        return "NO"

n = int(input())
s = input()
print(is_pangram(n, s))'''

'''t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    isInc = True
    for i in range(n-1):
        if a[i] == a[i+1]:
            isInc = False
            break
    if isInc:
        print("YES")
    else:
        print("NO")'''

#MATRICES

'''A = [[1,2,3], [3,4,5], [3,4,6]]
B = [[2,4,5], [5,4,3], [0,4,3]]
C = [[0 for i in range(len(A))] for j in range(len(A[0]))] # Product
D = [[0 for i in range(len(A))] for j in range(len(A[0]))] #Transpose
sum_diagonal = 0
sum_diagonal_2 = 0
print(C)
for i in range(len(A)):
    sum_diagonal += A[i][i]
    sum_diagonal_2 += A[i][len(A)- i - 1]


print(A)
print(sum_diagonal + sum_diagonal_2)'''

'''n = int(input())
A = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        A[i][i] = 1
for i in A:
    print(i)'''

'''A = [[1,2,3], [3,4,5], [3,4,6]]
n = len(A)
print("Upper Triangular Matrix")
for i in range(n):
    for j in range(i,n):    
        print(A[i][j], end = " ")
    print()

print("Lower Triangular Matrix")
for i in range(n):
    for j in range(i+1):
        print(A[i][j], end = " ")
    print()'''

'''def evaluate(s):
    temp_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five': 5, 'six':6, 'seven':7, 'eight':8, 'nine': 9}
    s.split()
    ans = 0
    for i in range(0,len(s),2):
        if s[i] =='plus':
            ans += temp_dict[s[i+1]]
        elif s[i] == 'minus':
            ans -= temp_dict[s[i+1]]
        else:
            if i == 0:
                ans = temp_dict[s[i]]
            else:
                if s[i-1] == 'plus':
                    ans += temp_dict[s[i]]
                elif s[i-1] == 'minus':
                    ans -= temp_dict[s[i]]
    return ans

print(evaluate("minus one plus two minus three"))'''

'''def longestConsecutive(nums):
    n = len(nums)
    if n == 0:
        return 0

    longest = 1
    st = set()

    for i in range(n):
        st.add(nums[i])
    
    for it in st:
        if it - 1 not in st:
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest'''

'''k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

arr = []

for i in range(1,d+1):
    if i % k == 0:
        arr.append(i)
    elif i % l == 0:
        arr.append(i)
    elif i % m == 0:
        arr.append(i)
    elif i % n == 0:
        arr.append(i)

a = len(arr)
print(a)'''

'''class Node:

    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

arr = [2,1,3,8]

def array_to_ll(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = mover.next
    
    return head

def traversal(head):
    temp = head
    while temp.next != None:
        print(temp.data, end = " -> ")
        temp = temp.next
    print(temp.data)'''

#traversal(array_to_ll(arr))

'''def count(head):
    temp = head
    cnt = 0
    while temp != None:
        cnt += 1
        temp = temp.next
    
    print(cnt)

count(array_to_ll(arr))'''

'''def search(head, val):
    temp = head
    while temp != None:
        if temp.data == val:
            return True
        temp = temp.next

    return False

print(search(array_to_ll(arr), 0))'''



'''from collections import defaultdict


def countch(words, chars):
    counts = defaultdict(int)
    for c in chars:
        counts[c] += 1
    
    print(counts)
    ans = 0
    for word in words:
        word_count = defaultdict(int)
        for c in word:
            word_count[c] += 1

        fine =  True
        for key, val in word_count.items():
            if counts[key] < val:
                fine = False
                break
        if fine:
            ans += len(word)
    
    print(ans)

countch(["hello","world","leetcode"],"welldonehoneyr")'''
'''class Node:
    def __init__(self, data, next_node = None, back_node = None):
        self.data = data
        self.next = next_node
        self.back = back_node


def convert_arr_to_dll(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp

    return head

def print_dll(head):
    while head is not None:
        print(head.data, end = " ")
        head = head.next
 

def reverse_dll(head):
    if head is None or head.next is None:
        return head
    
    prev = None
    current = head
    while current != None:
        temp = current.next
        current.next = current.back
        current.back = temp
        prev = current
        current = current.back
    return prev

print_dll((reverse_dll(convert_arr_to_dll([4,3,2,1]))))'''

'''def minTimeToVisitAllPoints(points):
    time = 0
    for i in range(len(points)-1):
        x, y = points[i]
        end_x, end_y = points[i+1]
        mydist_x, mydist_y = abs(end_x - x), abs(end_y - y)
        time += max(mydist_x, mydist_y)
    
    print(time)

minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])'''

'''x = 'hello'
lst = []
lst.append(x[0].upper())
for ch in range(1, len(x)):
    lst.append(x[ch])

print(lst)'''

'''def largestGoodInteger(num):
    ans = ""
    for i in range(2, len(num)):
        if num[i-2] == num[i-1] == num[i]:
            ans = max(ans, num[i]*3)
    return ans

print(largestGoodInteger("6777133339"))'''
'''
def totalMoney(n):
    money = 0
    monday = 1
    while n > 0:
        for i in range(n):
            money += monday 
        n -= 7
        monday += 1
    return money
        '''

'''class Multiset:
    
    def __init__(self):
        self.lst = []

    def add(self, val):
        if val not in self.lst:
            self.lst.append(val)
    
    def remove(self, val):
        if val in self.lst:
            self.lst.remove(val)
    
    def __contains__(self, val):
        if val in self.lst:
            return True
        else:
            return False
    
    def __len__(self):
        return len(self.lst)'''


'''class Rectangle:

    def __init__(self, l,b):
        self.l = l
        self.b = b
    
    def area(self):
        return (self.l * self.b)

class Circle:

    def __init__(self, r):
        self.r = r
    
    def area(self):
        return (3.14 * self.r * self.r)'''

'''def transformSentence(sentence):
    lst = sentence.split()
    ans = ""
    for word in lst:
        ans += transform_help(word)
    return ans.rstrip()

def transform_help(word):
    ans = ""
    ans += word[0]
    for i in range(len(word)-1):
        y, x = i, i+1
        if ord(word[y].lower()) < ord(word[x].lower()):
            ans += word[x].upper()
        elif ord(word[y].lower()) > ord(word[x].lower()):
            ans += word[x].lower()
        elif ord(word[y].lower()) == ord(word[x].lower()):
            ans += word[x]
    ans += " "
    return ans


def avg(*args):
    n = len(args)
    summ = 0
    for num in range(len(args)):
        summ += args[num]
    ans = float(summ/n)
    return ans
'''

'''def numSpecial(mat):
    for i in range(len(mat)):
        cnt1 = 0
        for j in range(len(mat[0])):
            cnt = 0
            if mat[i][j] == 1:
                cnt += 1
        if cnt == 1:
            cnt1 += cnt
    
    print(cnt1)

numSpecial([[1,0,0],[0,1,0],[0,0,1]])'''
    
'''word = input().split()
final = ""
for i in word:
    temp = ""
    new = i.lower()
    temp += new[0].upper()
    temp += new[1:len(new)]
    final += temp
print(final)
'''

def good_years(papers):
    maxi = 0
    for i in papers:
        if i[1] > maxi:
            maxi = i[1]
    years = []
    for i in papers:
        if i[i] == maxi:
            years.append(i[0])
    return years


def fib(n):
    if n == 1:
        return 'a'
    elif n == 2:
        return 'b'
    else:
        return fib(n-2) + fib(n-1)

print(fib(4))

def inverse(s):
    for i in range(1,100):
        if fib(i) == s:
            return i
        
print(inverse('bab'))