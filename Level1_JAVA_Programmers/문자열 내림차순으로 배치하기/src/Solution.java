import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";

        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        for (int i = arr.length-1;i > -1; i--) {
            answer += arr[i];
        }
        return answer;
    }
}