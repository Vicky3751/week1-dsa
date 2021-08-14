class Solution:
    def addDigits(self, num: int) -> int:
        n = 1+(num-1)%9
        if(num==0):
            return 0
        else:
            return n
