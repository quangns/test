'''
Thuat toan Quy hoach dong

Cho day n so nguyen a1, a2, ..., an. Hay tim 2 chi so i,j sao cho i < j
va hieu aj - ai la lon nhat

Dữ liệu vào:
- Danh sách n số nguyên a1, a2, ..., an (0 ≤ ai ≤ 109)

Dữ liệu xuất:
- Là giá trị lớn nhất của hiệu aj - ai.
'''

import time


def HISO(data):
    hieuso = 0
    min = 9999999
    for number in data:
        if number < min:
            min = number
        elif (number - min) > hieuso:
            hieuso = number - min
    return hieuso


if __name__ == '__main__':
    start_time = time.time()
    print(start_time)
    hieuso = HISO([10, 5, 6, 8, 9, 11, 35, 1, 12, 34, 3])
    end_time = time.time()
    print(end_time)
    print(hieuso)
    print('total run-time: %f ms' % ((end_time - start_time) * 1000))
