class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            arr=[]
            y=str(abs(x))
            for num in y:
                l=int(num)
                arr.append(l)
            if x<0:
                arr[0]=arr[0]*-1
            
            rev_arr=arr[::-1]
        
        return arr==rev_arr