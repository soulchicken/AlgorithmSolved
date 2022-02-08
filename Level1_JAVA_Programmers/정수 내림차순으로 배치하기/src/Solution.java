class Solution {
    public long solution(long n) {
        int[] arr = {0,0,0,0,0,0,0,0,0,0};

        while (n != 0) {
            arr[(int) (n % 10)] += 1;
            n /= 10;
        }

        String answer = "";

        for (int i = 9; i > -1; i--) {
            while (arr[i] != 0) {
                answer = answer + i;
                arr[i] -= 1;
            }
        }

        return Long.parseLong(answer);
    }
}