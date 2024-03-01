l = [1, 2, 3, 4, 5, 6, 7, 8]


def reverse(lst):
    start_index = 0
    end_index = len(l) - 1

    while end_index > start_index:
        l[start_index], l[end_index] = l[end_index], l[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

if __name__ == '__main__':
    reverse(l)
    print(l)




