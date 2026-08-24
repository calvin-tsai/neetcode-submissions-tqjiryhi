class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # local name: remove periods and everything after '+'
        # domain name: nothing
        # normalize all emails and add to set, then return len(set)

        res = set()

        for email in emails:
            # divider = email.find("@")
            # local = email[0 : divider]
            # domain = email[divider : ]
            local, domain = email.split("@")

            local = local.replace(".", "")
            # firstPlus = local.find("+", len(local))
            # local = local[0 : firstPlus]
            local = local.split("+")[0] # split by "+", get first 

            res.add(f"{local}@{domain}")

        # print(res)
        return len(res)