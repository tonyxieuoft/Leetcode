class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dct = [None]*(len(s)+1)
        for i in range(len(s)+1):
            dct[i] = [None]*(len(p)+1)

        matchHelper(s, p, 0, 0, dct)
        return dct[0][0]


def matchHelper(s, p, i, j, dct):
    # check if both go over, just in case
    if i == len(s) and j == len(p):
        dct[i][j] = True
    elif i == len(s):
        if len(p) - j > 1 and p[j+1] == "*":
            if dct[i][j+2] is None:
                matchHelper(s, p, i, j+2, dct)
            dct[i][j] = dct[i][j+2]
        else:
            dct[len(s)][j] = False
    elif j == len(p):
        dct[i][len(p)] = False
    else:
        if len(p) - j > 1 and p[j+1] == "*":
            star = True
        else:
            star = False
        if not star:
            if p[j] != "." and s[i] != p[j]:
                dct[i][j] = False
            else:
                if dct[i+1][j+1] is None:
                    matchHelper(s, p, i+1, j+1, dct)
                dct[i][j] = dct[i+1][j+1]
        else:
            if p[j] != "." and s[i] != p[j]:
                if dct[i][j+2] is None:
                    matchHelper(s, p, i, j+2, dct)
                dct[i][j] = dct[i][j+2]
            else:
                if dct[i][j+2] is None:
                    matchHelper(s, p, i, j+2, dct)
                if dct[i+1][j+2] is None:
                    matchHelper(s, p, i+1, j+2, dct)
                if dct[i+1][j] is None:
                    matchHelper(s, p, i+1, j, dct)
                dct[i][j] = dct[i][j+2] or dct[i+1][j+2] or dct[i+1][j]
