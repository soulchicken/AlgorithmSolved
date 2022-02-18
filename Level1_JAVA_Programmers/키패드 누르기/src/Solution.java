import java.util.Objects;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int[] leftHand = {3,0};
        int[] rightHand = {3,2};
        int button0;
        int button1;

        int rightGap;
        int leftGap;
        for (int num : numbers) {
            if (num % 3 == 1) {
                // 왼손
                leftHand[0] = num/3;
                leftHand[1] = 0;
                answer += "L";
            } else if (num != 0 && num % 3 == 0) {
                // 오른손
                answer += "R";
                rightHand[0] = num/3 - 1;
                rightHand[1] = 2;
            } else {
                if (num == 0) {
                    button0 = 3;
                } else {
                    button0 = num / 3;
                }
                button1 = 1;

                rightGap = Math.abs(rightHand[0] - button0) + Math.abs(rightHand[1] - button1);
                leftGap = Math.abs(leftHand[0] - button0) + Math.abs(leftHand[1] - button1);
                if (rightGap < leftGap || (leftGap == rightGap && Objects.equals(hand, "right"))) {
                    answer += "R";
                    rightHand[0] = button0;
                    rightHand[1] = 1;
                } else {
                    answer += "L";
                    leftHand[0] = button0;
                    leftHand[1] = 1;
                }


            }
        }
        return answer;
    }
}