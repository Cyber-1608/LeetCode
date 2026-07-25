class Solution:
    def maxProduct(self, n: int) -> int:
        X=[]
        while n>0:
            last_digit=n%10
            X.append(last_digit)
            n=n//10
        if len(X)<2:
            return "No multiplier found"
        X.sort(reverse=True)
        return X[0] * X[1]
        