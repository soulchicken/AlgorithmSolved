class Solution {
    public int solution(int num) {
        int answer = 0;
        long n = (long) num;
        for (int i = 0; i < 500; i++) {
            if (n == 1) {
                return answer;
            }
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n *= 3;
                n++;
            }
            answer++;
        }
        return -1;
    }
}