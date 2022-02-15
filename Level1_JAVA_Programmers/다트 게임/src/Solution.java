class Solution {
    public int solution(String dartResult) {
        dartResult = dartResult.replaceAll("10","t");

        char[] num = {'0','1','2','3','4','5','6','7','8','9'};

        int[] arr = new int[3];
        char[] arr2 = dartResult.toCharArray();
        int index = 0;
        for (int i = 0; i < arr2.length; i++) {
            for (char word : num) {
                if (word == arr2[i]){
                    arr[index] = Integer.parseInt(String.valueOf(arr2[i]));
                    index++;
                    break;
                }
            }
            if (arr2[i] == 't') {
                arr[index] = 10;
                index++;
            } else if (arr2[i] == 'S') {
                arr[index-1] *= 1;
            } else if (arr2[i] == 'D') {
                arr[index-1] *= arr[index-1];
            } else if (arr2[i] == 'T') {
                arr[index-1] *= arr[index-1]*arr[index-1];
            } else if (arr2[i] == '#') {
                arr[index-1] *= -1;
            } else if (arr2[i] == '*') {
                arr[index-1] *= 2;
                if (index != 1) {
                    arr[index-2] *= 2;
                }
            }
        }
        return arr[0]+arr[1]+arr[2];
    }
}