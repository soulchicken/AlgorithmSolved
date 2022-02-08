class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        int a;
        int b;

        if (n < m) {
            a = m;
            b = n;
        } else {
            a = n;
            b = m;
        }

        while (b != 0) {
            int x = a;
            int y = b;
            a = y;
            b = x % y;
        }
        answer[0] = a;
        answer[1] = n*m/a;

        return answer;
    }
}