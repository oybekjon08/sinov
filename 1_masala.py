lst = ["salom", "dunyo", "nima", "gapla"]
max=lst[0]
for i in lst:
    if len(max)<len(i):
        max=i
print(max)