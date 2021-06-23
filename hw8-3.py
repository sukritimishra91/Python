def partition(start,end,input):
    left = start + 1
    right = end
    while left < right:
        while left < end and input[left] < input[start]:
            left = left + 1
        while right > start and input[right] > input[start]:
            right = right - 1
        if left < right:
            input[left],input[right] = input[right],input[left]
    input[start],input[right] = input[right],input[start]
    return right

def quickSort(start,end,input):
    if input is None or len(input) < 1:
        print('inputs incorrect')
    if start < end:
        pIndex = partition(start,end,input)
        quickSort(start,pIndex - 1,input)
        quickSort(pIndex + 1,end,input)


input = [54,26,93,17,77,31,44,55,20]
print(f'Before Sort - {input}')
quickSort(0,len(input) - 1,input)
print(f'After Sort - {input}')

input = [12,56,1,5,2,9,27]
print(f'Before Sort - {input}')
quickSort(0,len(input) - 1,input)
print(f'After Sort - {input}')
