class Solution(object):
    def reverse(self, x):
        if(-2147483648<x<2147483647):
            if(x<0):
                x=x*-1
                y=int(str(x)[::-1])
                y=y*-1
                if(-2147483648<y<2147483647):
                    return(y)
                else:
                    return 0
            else:
                y=int(str(x)[::-1])
                if(-2147483648<y<2147483647):
                    return(y)
                else:
                    return 0
        else:
            return 0
        