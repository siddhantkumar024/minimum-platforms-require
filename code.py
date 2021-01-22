def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    arr.sort()
    dep.sort()
    i=1
    j=0
    curr=1
    res=1
    while i<n and j<n:
        if arr[i]<=dep[j]:
            curr+=1
            i+=1
        elif(arr[i]>dep[j]) :
            curr-=1
            j+=1
        if (curr>res):
            res=curr
    return res
    
    
    
    
    
    
   """  For Input:
N=6 
0900 0940 0950 1100 1500 1800
0910 1200 1120 1130 1900 2000 
your output is:
3  """
