package N개의최소공배수;

class Solution {
    public int solution(int[] arr) {
        int answer = arr[0];
        for (int i = 1; i < arr.length; i++) {
            answer = makeLCM(answer,arr[i]);
        }
        return answer;
    }

    public int makeLCM(int n, int m) {
        int x = Math.max(n,m);
        int y = Math.min(n,m);
        int z;
        while (y != 0) {
            z = y;
            y = x % y;
            x = z;
        }
        return n*m/x;
    }
}