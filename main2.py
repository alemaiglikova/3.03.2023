def range_compress(list):
    list.sort()
    range = []
    i = 0
    while i < len(list):
        current_val = list[i]
        while i < len(list) - 1 and list[i+1] == list[i] + 1:
            i += 1
        if list[i] != current_val:
            range.append(str(current_val) + "-" + str(list[i]))
        else:
            range.append(str(current_val))
        i += 1
    return ",".join(range)