package Sep2024.MergeSortedArrays;

public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n==0)
            return;
        if (m==0) {
            System.arraycopy(nums2, 0, nums1, 0, nums2.length);
            return;
        }
        final int[] answerSorted = new int[m+n];

        int i1=0, i2=0;
        for (int i = 0; i < answerSorted.length; i++) {
            if (i2 == n || (i1 < m && nums1[i1] < nums2[i2]))
                answerSorted[i] = nums1[i1++];
            else
                answerSorted[i] = nums2[i2++];
        }

        System.arraycopy(answerSorted, 0, nums1, 0, nums1.length);
    }
}