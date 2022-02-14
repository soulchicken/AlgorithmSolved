import java.util.Arrays;

class Solution {
    public int solution(int[] nums) {
        Arrays.sort(nums);
        boolean[] check = new boolean[3000];

        for (int i = 2; i < 3000; i++) {
            if (!check[i]) {
                for (int j = i * 2; j < 3000; j += i) {
                    check[j] = true;
                }
            }
        }

        int answer = 0;

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    if (!check[nums[i] + nums[j] + nums[k]]) {
                        answer++;
                    }
                }

            }
        }
        return answer;
    }

}