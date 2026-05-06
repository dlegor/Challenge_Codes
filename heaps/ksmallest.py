from typing import List, Any
from heapq

class Solution:

    def kth_smallest(self,arr:List[int],k:int):
        #sort list
        arr=sorted(arr)

        return arr[k-1]
#O(nlog(n))
    def kth_smallest2(self,arr:List[int],k:int):
        #sort list
        max_list=[]

        for elem in arr:
            

        arr=sorted(arr)

        return arr[k-1]





if __name__=='__main__':

    arr,k =  [7, 10, 4, 3, 20, 15], 3 
    print("#"*100)

    print(Solution().kth_smallest(arr,k))