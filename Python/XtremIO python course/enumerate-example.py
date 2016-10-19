s = "what da fuck ?!"
for x in enumerate(s):
    print(x)

# pay attention to unpacking in the loop and output !
k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for e, v in enumerate(k):
    print e, v

# good example for graphs based on data in tuple
data = [
    10,
    3,
    4,
    8,
    16,
    4,
    2,
    0,
    10,
    4,
    3,
    16,
    16,
]
maxValueinData = max(data)
for x in data:
    if x == maxValueinData:
        print(x * "*")
    else:
        print(x * "=")
