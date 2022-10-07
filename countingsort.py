def counting(data):
    counts = [0 for i in range(max(data)+1)]
    print(counts)
    for value in data:
        counts[value] += 1
    print(counts)    
    for index in range(1, len(counts)):
        counts[index] = counts[index-1] + counts[index]
    print(counts)
    arr = [0 for loop in range(len(data))]
    for value in data:
        index = counts[value] - 1
        arr[index] = value
        counts[value] -= 1
    return arr
data = [2, 7, 16, 20, 15, 1, 3, 10]
print(counting(data))
