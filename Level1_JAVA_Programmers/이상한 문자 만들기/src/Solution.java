class Solution {
    public String solution(String s) {
        char[] arr = s.toCharArray();
        String answer = "";
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == ' ') {
                count = 0;
                answer += ' ';
            }
            else {
                if (count % 2 == 0) {
                    answer += Character.toUpperCase(arr[i]);
                } else {
                    answer += Character.toLowerCase(arr[i]);
                }
                count++;
            }
        }
        return answer;
    }
}