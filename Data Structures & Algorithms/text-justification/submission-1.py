class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # take words until it overflows (total length > 16) then that word 
        # is in the next line

        # to space the words - subtract length of words from maxwidth and 
        # divide evenly by (numwords - 1), with remainder going on left
        # if theres only one word per line, add spaces to the end

        # last row ( if len words < maxwidth) then add it all in and add remaining spaces at end
        
        res = []
        line = []
        line_len = 0
        # loop through words list O(n) time
        for w in words: 
            # if next word would overflow, add curr to res
            if len(w) + line_len + len(line) > maxWidth:
                if len(line) == 1:
                    # add remainder spaces to the end if only one
                    res.append(line.pop(0) + " " * (maxWidth - line_len))
                else:
                    space_left = maxWidth - line_len - len(line) + 1
                    to_add = ""
                    while line:
                        # grab the word, divide spaces, update space left, add word and space
                        word = line.pop(0)
                        if len(line) > 0:
                            space = math.ceil(space_left / len(line))
                            space_left -= space
                            to_add += word + " " * (space + 1)
                        else:
                            to_add += word
                    res.append(to_add)
                line_len = 0
            line.append(w)
            line_len += len(w)
        # if there's still words left, add them all to the end
        last_line = ""
        for i in range(len(line)):
            last_line += line[i]
            if i != len(line) - 1:
                last_line += " "
        last_line += " " * (maxWidth - line_len - len(line) + 1)
        res.append(last_line)
        
        return res
                    
            
