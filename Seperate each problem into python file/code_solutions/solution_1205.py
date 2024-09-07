def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def main():
    arr = [12, 11, 13, 5, 6, 7]
    print(sort(arr))

if __name