# quicksortfunction
def quicksort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr

# sorting the array in this function
def qs(arr, low, high):
    if low < high:
        partition = part_fun(arr, low, high)
        qs(arr, low, partition - 1)
        qs(arr, partition + 1, high)

# partition function to place pivot at right place
def part_fun(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high -1:
            i += 1
        
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

# main function
def main():
    n = input()
    arr = list(map(int, n.split(" ")))
    sorted_array = quicksort(arr)
    print(str(sorted_array))

if __name__ == '__main__':
    main()