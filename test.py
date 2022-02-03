text = open("task5.txt", "r")

count_names = {}
for name in text:
    if name in count_names:
        count_names[name] += 1
    else:
        count_names[name] = 1

print(count_names) 