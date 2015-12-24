####What dominates your array###
def dominator(arr):
    metric=len(arr)/2
    status=-1
    for i in arr:
        #print arr.count(i)
        if arr.count(i)<=metric:
            continue
        else:
            status=i
    
    return status
            
if __name__=="__main__":
    print dominator([1,1,1,2,2,2,2])
