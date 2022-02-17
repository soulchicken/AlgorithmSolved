import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("출력 : " + Arrays.toString(s.solution(5,new int[] {2, 1, 2, 6, 2, 4, 3, 3})));
        System.out.println("답안 : [3, 4, 2, 1, 5]");
        System.out.println("출력 : " + Arrays.toString(s.solution(4,new int[] {4, 4, 4, 4, 4})));
        System.out.println("답안 : [4, 1, 2, 3]");
        System.out.println("출력 : " + Arrays.toString(s.solution(5,new int[] {1, 2, 2, 1, 3})));
        System.out.println("답안 : [3, 2, 1, 4, 5]");
        System.out.println("출력 : " + Arrays.toString(s.solution(5,new int[] {2, 1, 2, 4, 2, 4, 3, 3})));
        System.out.println("답안 : [4, 3, 2, 1, 5]");
    }
}