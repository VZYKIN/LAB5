Print('Это функция, которая считает медиану двух отсортированных списков, введите два массива.')
def findMedian(self, nums1, nums2):
        VZ=nums1+nums2
        VZ.sort()
        n=len(VZ)
        if len(VZ)==0 or len(VZ)==1:
            return VZ[0]
        if n%2!=0:
            s=(n/2)
            return VZ[s]
        else:
            return (VZ[n/2]+VZ[(n/2)-1])/2.0
