def count_words():
    ip = "abbaccacacc"
    count = {}
    for i in ip:
        count[i] = count.get(i,0) + 1

    sorted_by_value = sorted(count.items(), key=lambda kv: kv[1])[::-1]
    ans = ''
    for i in sorted_by_value :
        ans += str(i[1]) + i[0]

    print(ans)

def flatten_list():
    t = [[1,2,3],[4,5],[6,7,9]]
    # ans = [item for sublist in t for item in sublist]


def binary_search():
    test = [1,3,4,5,6,6,9]
    left, right, target = 0, len(test) - 1, 2
    while right >= 1:
        mid = (left + right) // 2
        if test[mid] == target:
            return True
        elif test[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == "__main__":
    count_words()
    print(binary_search())
