import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        int answer = nums.length / 2;
        Set<Integer> hash = new HashSet<>();
        for (int i : nums) {
            hash.add(i);
        }
        if (hash.size() < answer) {
            answer = hash.size();
        }
        return answer;
    }
}