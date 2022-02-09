import java.util.Arrays;

class Solution {
    public int solution(int n) {
        int[] arr = new int[n+1];
        for (int i = 2; i < n+1; i++) {
            if (arr[i] == 0) {
                for (int j = i*2; j < n+1; j += i) {
                    arr[j] = 1;
                }
            }
        }
        int answer = arr.length - Arrays.stream(arr).sum() - 2;
        return answer;
    }
}