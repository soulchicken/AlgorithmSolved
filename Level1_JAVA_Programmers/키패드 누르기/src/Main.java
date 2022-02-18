public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("출력 : " + s.solution(new int[]{1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5}, "right"));
        System.out.println("해답 : LRLLLRLLRRL");
        System.out.println("출력 : " + s.solution(new int[]{7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2}, "left"));
        System.out.println("해답 : LRLLRRLLLRR");
        System.out.println("출력 : " + s.solution(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}, "right"));
        System.out.println("해답 : LLRLLRLLRL");
    }
}