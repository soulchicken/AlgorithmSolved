class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i < right+1; i++) {
            double num = Math.sqrt(i);
            if (num == (int) num) {
                answer -= i;
            } else {
                answer += i;
            }
        }
        return answer;
    }
}