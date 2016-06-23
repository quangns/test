def selection_sort(data):
    for i in range(len(data)):
        min = data[i]
        index = i
        for compared_index in range(i+1,len(data)):
            if min > data[compared_index]:
                min = data[compared_index]
                index = compared_index

        if index != i:
            min = data[i]
            data[i] = data[index]
            data[index] = min
    return data


if __name__ == '__main__':
    print selection_sort([10, 5, 6, 8, 9, 11, 3, 1, 12, 34, 35])