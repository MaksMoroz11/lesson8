# def bin_poisk(arr, threat, min_val, high_val):
#     if high_val < min_val:
#         return -1  # Не верный диапазон
#     mid_val = (high_val + min_val) // 2
#
#     if arr[mid_val] == threat:
#         return mid_val
#     if threat < arr[mid_val]:
#         return bin_poisk(arr, threat, min_val, mid_val - 1)
#     if threat > arr[mid_val]:
#         return bin_poisk(arr, threat, mid_val + 1, high_val)
#
#
# list1 = [-124, -25, 123, 248, 249, 427, 2154]
# threat = -25
#
# print(bin_poisk(list1, threat, 0, len(list1)))

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
#
# def even_to_zero(_list):
#     for i in range(len(_list)):
#         if _list[i] % 2 == 0:
#             _list[i] = 0
#     return _list
#
#
# list1 = even_to_zero(list1)

a, b = 7, 4


def huge_to_zero(a, b):
    c= 1
    if a > b:
        a = 0
    elif b > a:
        b = 0


print(a, b)
