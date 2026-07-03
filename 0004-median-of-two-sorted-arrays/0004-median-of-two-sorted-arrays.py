class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n=len(nums1)
        m=len(nums2)
        a=[]
        for i in range(n):
            a.append(nums1[i])
        for j in range(m):
            a.append(nums2[j])
        a.sort()
        k=len(a)
        l=len(a)//2
        if(k%2==0):
            p=l-1
            u=(a[p]+a[l])/2.0
            return u
        else:
            return a[l]