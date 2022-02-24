package 땅따먹기;

class Solution {
    int solution(int[][] land) {
        int answer;
        bestWayLand(land);
        answer = findMax(land[0]);
        return answer;
    }

    private void bestWayLand(int[][] land) {
        for (int i = land.length-2; i > -1; i--) {
            for (int j = 0; j < 4; j++) {
                land[i][j] += findMax(land[i+1],j);
            }
        }
    }

    public static int findMax(int[] landIndexZero) {
        int num = 0;
        for (int i : landIndexZero) {
            if (num < i) {
                num = i;
            }
        }
        return num;
    }

    public static int findMax(int[] landIndex,int index) {
        int num = 0;
        for (int i = 0; i < 4; i++) {
            if (i != index && num < landIndex[i]) {
                num = landIndex[i];
            }
        }
        return num;
    }
}
