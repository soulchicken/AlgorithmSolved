import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public Integer[] solution(int[] numbers) {
        HashSet<Integer> hash = new HashSet<>();
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                hash.add(numbers[i]+numbers[j]);
            }
        }
        Integer[] answer = hash.toArray(new Integer[0]);
        Arrays.sort(answer);
    return answer;
    }
}