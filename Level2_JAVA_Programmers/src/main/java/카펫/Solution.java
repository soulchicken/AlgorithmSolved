package 카펫;

class Solution {
    public int[] solution(int brown, int yellow) {
        brown += yellow;
        int[] answer = new int[2];
        for (int i = 1; i < yellow + 1; i++) {
            if (yellow % i == 0 && brown % (i+2) == 0 && (yellow/i + 2) == (brown/(i+2))) {
                return new int[] {(brown / (i+2)),i+2};
            }
        }
        return answer;
    }
}