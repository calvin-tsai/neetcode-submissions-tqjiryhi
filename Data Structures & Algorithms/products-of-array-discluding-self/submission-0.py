class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # question: is the array sorted? 
        # brute force, iterate through array, then iterate through each other element and multiply
        # this is O(n^2) time
        # To prevent multiple calculations, we can keep track of our current staet
        # 2 * 24, 1 * 24, 2 * 6, 2 * 4
        # first half and second half approach: calculate product of first half, iterate through second half
        # calculate product of second half, iterate through first half
        # with division operation: find total product and divide by nums[i]

        prod = 1
        for n in nums: #total product
            prod = prod * n
        res = []
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(prod // nums[i])
            else: #brute force, worst case we have O(n^2)
                newProd = 1
                for j in range(len(nums)):
                    if j == i:
                        continue
                    newProd *= nums[j]
                res.append(newProd)
        return res
        

