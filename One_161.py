class One_161:
    # Standard solution
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if abs(ns - nt) > 1 or s == t:
            return False
        if ns > nt:
            return self.isOneEditDistance(t, s)
        for i in range(ns):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] if ns == nt else s[i:] == t[i+1:]
        return True
    # My first solution
    # def isOneEditDistance(self, s: str, t: str) -> bool:
    #     if abs(len(s) - len(t)) > 1 or s == t:
    #         return False
    #     if len(s) > len(t):
    #         return self.isOneEditDistance(t, s)
    #     if len(s) == len(t):
    #         mismatch = 0
    #         for i in range(len(s)):
    #             if s[i] != t[i]:
    #                 mismatch += 1
    #                 if mismatch > 1:
    #                     return False
    #         return True
    #     i, mismatch = 0, 0
    #     for j in range(len(t)):
    #         if i == len(s) or s[i] != t[j]:
    #             mismatch += 1
    #             if mismatch > 1:
    #                 return False
    #         else:
    #             i += 1
    #     return True