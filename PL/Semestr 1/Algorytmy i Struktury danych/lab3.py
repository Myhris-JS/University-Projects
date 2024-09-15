#zadanie 1
def collatz(n):
    print(n)
    if n == 1:
        return
    elif n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)
collatz(5)


#zadanie 2
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(48, 18))
print(gcd(60, 48))


#zadanie 3
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)
arr_to_sort = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr_to_sort)
print(sorted_arr)

#zadanie 4
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

arr_to_sort = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr_to_sort)
print("Posortowana lista:", sorted_arr)