def quick_sort(data, first, last):
    pivot = data[first]
    leftmark = first + 1
    rightmark = last
    while leftmark <= rightmark:
        while data[leftmark] < pivot:   #tim phan tu ben trai > key
            leftmark += 1
        while data[rightmark] > pivot:  #tim phan tu ben phai < key
            rightmark -= 1
        if leftmark < rightmark:
            tmp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] =tmp
    if pivot > data[rightmark]:
        tmp = data[first]
        data[first] = data[rightmark]
        data[rightmark] = tmp
    if first < rightmark:
        quick_sort(data, first, rightmark-1)
    if leftmark < last:
        quick_sort(data, leftmark, last)
    return data

if __name__ == '__main__':
    data =[10, 5, 14, 12, 9, 11, 3, 1, 8, 34, 35]
    print quick_sort(data, 0, len(data) -1)