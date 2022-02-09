class Solution {
    public long solution(long n) {
        double num = Math.sqrt((double) n);
        if (num == (int) num) {
            num += 1;
            return ((long) num) * ((long) num);
        } else {
            return -1;
        }
    }
}