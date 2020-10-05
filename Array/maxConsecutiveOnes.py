"""
    Find count of maximum consecutive 1s in a binary array. 
    Eg: 
        arr = [0, 1, 1, 0, 1]
        maximum consecutive 1s = 2 [from index 1 to 2]
    
    Solution:
        Time complexity : O(n)
        Space complexity: require O(1) auxiliary space.
"""

def max_consecutive_ones(arr, size):
    count, res = 0, 0
    
    for i in range(size):
        if arr[i] == 1:
            count += 1 
            res = max(res, count)
        else:
            if count != 0 :
                count = 0
                
    return res
    

if __name__ == '__main__':
    
     arr = [0, 1, 1, 0, 1]
     n = len(arr)
     
     result = max_consecutive_ones(arr, n)
     print(result)
