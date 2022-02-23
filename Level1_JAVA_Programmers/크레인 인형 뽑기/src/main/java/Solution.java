import java.util.ArrayList;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Integer> stack = new ArrayList<>();
        stack.add(101);
        stack.add(102);
        for (int move : moves) {
            for (int i = 0; i < board.length; i++) {
                if (board[i][move-1] != 0) {
                    stack.add(board[i][move-1]);
                    board[i][move-1] = 0;
                    if (stack.get(stack.size() - 1).equals(stack.get(stack.size() - 2))) {
                        stack.remove(stack.size() - 1);
                        stack.remove(stack.size() - 1);
                        answer += 2;
                    }
                    break;
                }
            }
        }
        return answer;
    }
}