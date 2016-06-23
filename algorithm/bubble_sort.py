def bubble_sort(data):
    for x in range(len(data)):
        for i in range(len(data)-1, x,-1):
            if data[i] < data[i-1]:
                target = data[i]
                data[i] = data[i-1]
                data[i-1] = target
    return data

if __name__ == '__main__':
    print bubble_sort([10, 5, 6, 8, 9, 11, 35, 1, 12, 34, 3])