from random import randint


def quick_sort(data):
    left_data = []
    right_data = []

    if len(data) == 2:
        if data[0] > data[1]:
            tmp = data[0]
            data[0] = data[1]
            data[1] = tmp

    elif len(data) > 2:
        index = randint(0,len(data)-1)
        for x in range(len(data)):
            if x == index:
                continue
            else:
                if data[x] > data[index]:
                    right_data.append(data[x])
                else:
                    left_data.append(data[x])

        length = len(left_data)
        data[len(left_data)] = data[index]
        quick_sort(left_data)
        quick_sort(right_data)
        for i in range(length):
            data[i] = left_data[i]
        for i in range(len(right_data)):
            data[length+i+1] = right_data[i]
    return data


if __name__ == '__main__':
    print quick_sort([10, 5, 6, 8, 9, 11, 3, 1, 12, 34, 35])
