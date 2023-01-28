'''
- 리스트에서 사용 가능
- 반드시 reference 리스트는 정렬해주어야함
'''

# For 문

def BinarySearch_for(arr, target):
    low = 0
    high = len(arr) - 1

    while low<= high:
        mid = int((low + high) / 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def BinarySearch_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = int((low + high) / 2)

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearch_recursive(arr, target, low, mid-1)
    else:
        return BinarySearch_recursive(arr, target, mid+1, high)