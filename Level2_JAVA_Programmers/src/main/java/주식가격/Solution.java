package 주식가격;

class Solution {
    public int[] solution(int[] prices) {
        int count;
        int[] answer = new int[prices.length];
        for (int i = 0; i < prices.length; i++) {
            count = 0;
            for (int j = i+1; j < prices.length; j++) {
                count++;
                if (prices[i] > prices[j]) {
                    break;
                }
            }
            answer[i] = count;
        }
        return answer;
    }
}