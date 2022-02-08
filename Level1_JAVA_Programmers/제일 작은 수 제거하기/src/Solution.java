class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {
            return new int[] {-1};
        } else {
            int[] answer = new int[arr.length - 1];

            int index = 0;
            int min = arr[0];
            for (int i = 0; i < arr.length; i++) {
                if (min > arr[i]) {
                    index = i;
                    min = arr[i];
                }
            }

            for (int j = 0; j < index; j++) {
                answer[j] = arr[j];
            }
            for (int j = index + 1; j < arr.length; j++) {
                answer[j-1] = arr[j];
            }

            return answer;
        }
    }
}