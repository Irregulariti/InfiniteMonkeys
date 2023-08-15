from random import randint

if __name__ == "__main__":

    n = int(input("Length of the generated text: "))
    target = input("Target string: ").lower().strip()
    k = input("Skip or write custom count of copies(100 default): ")

    if k.isdigit():
        k = int(k)
    else:
        k = 100

    start_string: str
    target_length = len(target)

    choose = {}

    for _ in range(k):
        temp = "".join([chr(randint(97, 122)) for _ in range(n)])
        oldCount = 0
        index = 0
        for i in range(n - target_length + 1):
            curCount = 0
            for j in range(target_length):
                if temp[i + j] == target[j]:
                    curCount += 1
            if curCount > oldCount:
                oldCount = curCount
                index = i
        if oldCount != 0:
            choose[oldCount] = (temp, index)

    start_string, index = choose[max(choose.keys())]
    start_string_list = list(start_string)
    count = 0
    for i in range(index, target_length + index):
        if start_string_list[i] == target[i - index]:
            start_string_list[i] = start_string_list[i].upper()
            count += 1
    start_string = "".join(start_string_list)

    if count == target_length:
        ...  # very luck

    print(start_string)
    print(count)
