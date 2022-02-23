package 다리를_지나는_트럭;

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int inWeight = 0;
        Queue<Integer> bridge = new LinkedList<>();
        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }

        for (int truck : truck_weights) {
            for (int i = 0; i < bridge_length; i++) {
                answer++;
                inWeight -= bridge.remove();
                if (inWeight + truck > weight) {
                    bridge.add(0);

                } else {
                    inWeight += truck;
                    bridge.add(truck);
                    break;
                }
            }
        }
        return answer + bridge_length;
    }
}