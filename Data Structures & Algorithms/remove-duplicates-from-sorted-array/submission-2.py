class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # read index + write index problem similar to string compression
        # iterate through array, if nums[i] == nums[i+1] move until hit a new number then write that number
        # write index moves 1 by 1, read index moves by group
        # 1, 1, 1, 3, 3, 4, 4
        # 1, 3, 4


        read, write = 0, 0



        while read < len(nums):
            # write
            nums[write] = nums[read]
            
            # advance read to next group
            while read + 1 < len(nums) and nums[read] == nums[read + 1]:
                read += 1

            # advance write and read
            read += 1
            write += 1

        # ends up at the space just after its last write, = k
        return write
