def merge_sort(arr):
    if len(arr) > 1:
        left_array = arr[:len(arr)//2]
        right_array = arr[len(arr)//2:]

        merge_sort(left_array)
        merge_sort(right_array)
        i =  j = 0
        k = 0
        while  i < len(left_array) and j < len(right_array):

            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1
            
        while i < len(left_array):
            arr[k] = left_array[i]
            i  += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1

arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]

merge_sort(arr_test)
print(arr_test)
