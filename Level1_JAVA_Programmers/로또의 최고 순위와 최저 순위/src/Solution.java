class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] rank = {6, 6, 5, 4, 3, 2, 1};
        int zero = CountZero(lottos);
        int count = CountNum(lottos, win_nums);
        return new int[]{rank[count+zero],rank[count]};
    }

    public static int CountZero(int[] lottos) {
        int count = 0;
        for (int i : lottos) {
            if (i ==0) {
                count++;
            }
        }
        return count;
    }

    public static int CountNum(int[] lottos, int[] win_nums) {
        int count = 0;
        for (int i : lottos) {
            for (int j : win_nums) {
                if (i == j) {
                    count++;
                }
            }
        }
        return count;
    }
}
