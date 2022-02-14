class Solution {
    public int solution(int[][] sizes) {
        int min = 0;
        int max = 0;
        for (int[] size : sizes) {
            if (size[0] < size[1]) {
                if (min < size[0]) {
                    min = size[0];
                }
                if (max < size[1]) {
                    max = size[1];
                }
            } else {
                if (max < size[0]) {
                    max = size[0];
                }
                if (min < size[1]) {
                    min = size[1];
                }
            }
        }
        return min*max;
    }
}