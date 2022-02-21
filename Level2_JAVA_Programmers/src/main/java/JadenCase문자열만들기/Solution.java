package JadenCase문자열만들기;

class Solution {
    public String solution(String s) {
        String answer = "";
        boolean flag = false;
        for (int i = 0; i < s.length(); i++) {
            if (i == 0 || flag) {
                answer += String.valueOf(s.charAt(i)).toUpperCase();
             } else {
                answer += String.valueOf(s.charAt(i)).toLowerCase();
            }

            flag = s.charAt(i) == ' ';
        }
        return answer;
    }
}
