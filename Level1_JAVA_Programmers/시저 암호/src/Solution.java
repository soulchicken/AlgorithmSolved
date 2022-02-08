class Solution {
    public String solution(String s, int n) {
        char[] str = s.toCharArray();
        String answer = "";

        for (char word : str) {
            int x = (int) word;
            if (x > 64 && x < 91) {
                x += n;
                if (x > 90) {
                    x -= 26;
                }
            }

            if (x > 96 && x < 123) {
                x += n;
                if (x > 122) {
                    x -= 26;
                }
            }

            answer += (char) x;
        }
        return answer;
    }
}