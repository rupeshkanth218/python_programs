def binarysearch(itemlist,item):
    first=0
    last=len(itemlist)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2
        if itemlist[mid]==item:
            found=True
        else:
            if item< itemlist[mid]:
                last=mid-1
            else:
                first=mid+1
    return found

l=[3,4,5,6,7,8,9,10]
if binarysearch(l,3)==True:
    print("found")
else:
    print("not found")