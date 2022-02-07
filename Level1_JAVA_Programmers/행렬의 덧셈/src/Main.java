import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(Arrays.deepToString(solution.solution(new int[][] {{1, 2}, {2, 3}},new int[][]  {{3, 4}, {5, 6}})));
        System.out.println(Arrays.deepToString(solution.solution(new int[][] {{1}, {2}},new int[][]  {{3}, {4}})));
    }
}