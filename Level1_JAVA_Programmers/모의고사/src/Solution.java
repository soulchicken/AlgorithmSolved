import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
        int[] count = {0,0,0};
        int[] num1 = {1,2,3,4,5}; // 5개
        int[] num2 = {2,1,2,3,2,4,2,5}; // 8개
        int[] num3 = {3,3,1,1,2,2,4,4,5,5}; // 10개

        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == num1[i%5]) {
                count[0]++;
            }
            if (answers[i] == num2[i%8]) {
                count[1]++;
            }
            if (answers[i] == num3[i%10]) {
                count[2]++;
            }
        }

        int max = 0;
        for (int score : count) {
            if (max < score) {
                max = score;
            }
        }

        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            if (count[i] == max) {
                list.add(i+1);
            }
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}