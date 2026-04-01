class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        calcs = []
        for t in tokens:
            if t not in ops:
                calcs.append(t)
            else:
                arg2 = int(calcs.pop())
                arg1 = int(calcs.pop())
                if t == "+":
                    calcs.append(arg1 + arg2)
                elif t == "-":
                    calcs.append( arg1 - arg2)
                elif t == "*":
                    calcs.append( arg1 * arg2)
                else:
                    calcs.append(arg1 / arg2)
        return int(calcs.pop())