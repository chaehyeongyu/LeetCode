class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        merged_array = []
        l1 = nums1
        l2 = nums2

        while l1 != []:
            if l2 != []:
                if l1[0] < l2[0]:
                    merged_array += [l1[0]]
                    l1 = l1[1:]
                elif l1[0] > l2[0]:
                    merged_array += [l2[0]]
                    l2 = l2[1:]
                else:
                    merged_array += [l1[0]]
                    merged_array += [l2[0]]
                    l1 = l1[1:]
                    l2 = l2[1:]
            else:
                merged_array += l1
                break
        if l2 != []:
            merged_array += l2
        if len(merged_array) % 2:
            return float(merged_array[int((len(merged_array)-1)/2)])
        else:
            return float((merged_array[int(len(merged_array)/2)] + merged_array[int(len(merged_array)/2 - 1)])/2)
