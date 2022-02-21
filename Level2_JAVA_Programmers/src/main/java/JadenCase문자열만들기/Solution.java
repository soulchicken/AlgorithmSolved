package JadenCase문자열만들기;

class Solution {
    public String solution(String s) {
        String[] words = s.split(" ");
        String answer = "";
        for (int i = 0; i < words.length; i++) {
            if (i != 0) {
                answer += " ";
            }
            answer += makeJaden(words[i]);
        }
        return answer;
    }

    public String makeJaden(String str) {
        String first = str.substring(0,1).toUpperCase();
        first += str.substring(1).toLowerCase();
        return first;
    }
}
