class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)

        dct = [0]*len_s
        for i in range(len_s):
            dct[i] = [0]*len_s

        for diff in range(0, len_s):
            for i in range(0, len_s - diff):
                j = i + diff
                if diff == 0:
                    dct[i][j] = (i,j)
                elif diff == 1:
                    if s[i] == s[j]:
                        dct[i][j] = (i,j)
                    else:
                        dct[i][j] = (i,i)
                else:
                    if s[i] != s[j]:
                        t1 = dct[i][j-1]
                        t2 = dct[i+1][j]
                        if t1[1] - t1[0] > t2[1] - t2[0]:
                            dct[i][j] = t1
                        else:
                            dct[i][j] = t2
                    else:
                        t = dct[i+1][j-1]
                        if t[0] != i+1 or t[1] != j-1:
                            t1 = dct[i][j-1]
                            t2 = dct[i+1][j]
                            if t1[1] - t1[0] > t2[1] - t2[0]:
                                dct[i][j] = t1
                            else:
                                dct[i][j] = t2
                        else:
                            dct[i][j] = (i,j)

        r = dct[0][len_s-1]
        return s[r[0]:r[1]+1]


