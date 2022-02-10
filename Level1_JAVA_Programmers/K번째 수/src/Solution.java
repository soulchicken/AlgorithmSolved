import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        ArrayList<Integer> list = new ArrayList<>();
        for (int[] abc : commands) {
            int[] arr = Arrays.copyOfRange(array,abc[0]-1,abc[1]);
            Arrays.sort(arr);
            list.add(arr[abc[2]-1]);
        }
        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}