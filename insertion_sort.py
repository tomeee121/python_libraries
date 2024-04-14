def ins_sorting(listToSort):
    for j in range(1, len(listToSort)):
        valueToMove = listToSort[j]
        i=j-1
        while i >= 0 and listToSort[i]>valueToMove:
            listToSort[i+1] = listToSort[i]
            i-=1
        listToSort[i+1] = valueToMove

if __name__ == "__main__":
    listToSort = [0,4,2,200,100]
    ins_sorting(listToSort)
    print(listToSort)
