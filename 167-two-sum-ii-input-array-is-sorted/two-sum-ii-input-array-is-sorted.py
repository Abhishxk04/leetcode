class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=0
        b=len(numbers)-1
        c=[]
        while a<b:
            if numbers[a]+numbers[b]<target:
                a+=1
            elif numbers[a]+numbers[b]>target:
                b-=1
            elif numbers[a]+numbers[b]==target:
                c.append(a+1)
                c.append(b+1)
                break
            else:
                return (-1,-1)    
        return c                 
        