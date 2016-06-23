def merge_sort(data):
    if len(data) > 1:
        middle = len(data) / 2
        left_data = data[:middle]
        right_data = data[middle:]
        merge_sort(left_data)
        merge_sort(right_data)

        index, i, j =0, 0, 0
        while i <len(left_data) and j < len(right_data):
            if left_data[i] > right_data[j]:
                data[index] = right_data[j]
                j += 1
            else:
                data[index] = left_data[i]
                i += 1
            index += 1

        while i < len(left_data):
            data[index] = left_data[i]
            i += 1
            index += 1

        while j < len(right_data):
            data[index] = right_data[j]
            j += 1
            index += 1
    return data


if __name__ == '__main__':
    print merge_sort([10, 5, 6, 8, 9, 11, 3, 1, 12, 34, 35])