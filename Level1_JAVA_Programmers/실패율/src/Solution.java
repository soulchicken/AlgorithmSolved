import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

class Solution {
    public int[] solution(int N, int[] stages) {
        int peopleNum = stages.length;
        int[] inStage = new int[N+2];
        for (int i : stages) {
            inStage[i]++;
        }
//        System.out.println("inStage : " + Arrays.toString(inStage));

        HashMap<Integer, Double> failRate = new HashMap<>();
        for (int i = 1; i < N + 1; i++) {
            if (peopleNum == 0) {
                failRate.put(i,0.0);
            } else {
                failRate.put(i,((double) inStage[i]) / ((double) peopleNum));
            }
            peopleNum -= inStage[i];
        }
//        System.out.println("failRate : " + failRate);
        ArrayList<Double> rateArr = new ArrayList<>();
        for (int key : failRate.keySet()) {
             rateArr.add(failRate.get(key));
        }
        Collections.sort(rateArr, Collections.reverseOrder());
//        System.out.println("rateArr : " + rateArr);

        int[] answer = new int[N];
        int[] check = new int[N];

        for (int i = 0; i < N; i++) {
            // 사용할 것 : rateArr[i];
            for (Integer key : failRate.keySet()) {
                if (check[i] == 0 && rateArr.get(i) == failRate.get(key)) {
                    check[i] = 1;
                    answer[i] = key;
                }
            }
        }


        return answer;
    }
}