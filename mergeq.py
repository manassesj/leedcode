    def merge_sort(result, arr1, arr2, flag):
        if (len(arr1) + len(arr2)) > 1:
            if flag:
                left_array = arr1
                right_array = arr2
            else:
                left_array = arr1[:len(arr1) // 2]
                right_array = arr1[len(arr1) // 2:]

            merge_sort(result, left_array, [], False)
            merge_sort(result, right_array, [], False)

            i = j = 0
            k = 0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    result[k] = left_array[i]
                    i += 1
                    k += 1
                else:
                    result[k] = right_array[j]
                    j += 1
                    k += 1
            
            while i < len(left_array):
                result[k] = left_array[i]
                i += 1
                k += 1

            while j < len(right_array):
                result[k] = right_array[j]
                j += 1
                k += 1
        

    l1 = []
    l2 = [0]
    result = [None] * (len(l1) + len(l2))

    merge_sort(result, l1, l2, True)

    if len(l1) + len(l2) == 1:
        if len(l1) == 1:
            print(l1)
        else:
            print(l2)
    else:
        print(result)
