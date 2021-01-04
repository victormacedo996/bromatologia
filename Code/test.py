def test (first, second):
    x = first + second
    return x

list1 = [1, 2, 3, 4]
list2 = [2, 2, 2, 2]
list3 = []

for item1, item2 in zip(list1, list2):
    tey = test(item1, item2)
    list3.append(tey)

print(len(list3))
print(list3)