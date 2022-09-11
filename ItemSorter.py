# Take in list of items
items = input("Input items: ")
itemList = items.split(", ")


# Take in list of numbered items
f = open("FI_FFM.txt", 'r', encoding = "utf8")
numItems = {}
for line in f:
    line = line.replace("â€™", "'")
    k, v = line.strip().split('. ')
    numItems[k.strip()] = v.strip()
f.close()

# Print corresponding items
key_list = list(numItems.keys())
val_list = list(numItems.values())


for itemNum in range(len(itemList)):
    if itemList[itemNum] in key_list:
        print(str(itemList[itemNum]) + ". " + val_list[int(itemList[itemNum])-1])
