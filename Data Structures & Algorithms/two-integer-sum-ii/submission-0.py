class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        while(index1 < len(numbers)-1):
            diff = target - numbers[index1]
            for i in range(index1+1,len(numbers)):
                 if numbers[i] == diff:
                    return [index1+1,i+1]
            index1+=1
    