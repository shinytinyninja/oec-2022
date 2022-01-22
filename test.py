quarter = 3
half = 6

list = [1,2,3,4,5,6,7,8,9,10,11,12]
size = len(list)

print(list[0:quarter])
print(list[quarter:half])
print(list[half:half+quarter])
print(list[half+quarter:size])