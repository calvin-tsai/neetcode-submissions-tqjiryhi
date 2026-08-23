class Solution:
    def compress(self, chars: List[str]) -> int:
        # 'a' = 'a'
        # 'aa' = 'a','2'
        # multi-digit nums get broken down as well "12" = "1", "2" 
        # modify input array and return new length

        # idea: read and write pointer( compressed never exceeds lenght of noncompressed)
        
        # n not necessary since chars never changes len
        # all writes are in place O(1)
        n = len(chars)
        write = read = 0

        while read < n:
            # new read, chars[write] set to the character always
            chars[write] = chars[read]
            write += 1
            
            # find size of curr group
            # explore lands 1 away from group
            explore = read + 1
            while explore < n and chars[explore] == chars[read]:
                explore += 1 # on last, add the 
            
            # 2+ case, otherwise do nothing since explore alr read+1
            if explore - read > 1:
                for d in str(explore - read):
                    chars[write] = d
                    write += 1
            
            read = explore

        # write will finally sit at the end of compressed + 1, which happens to be the length of compressed!
        return write