package 프린터;

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[] priorities, int location) {
        int num = priorities[location];
        Queue<Integer> queue = new LinkedList<>();
        int[] nums = new int[10];
        for (int i : priorities) {
            queue.add(i);
            nums[i]++;
        }

        int count = 0;
        int answer = 0;
//         System.out.println("queue : " + queue + " | count : " + count + " | location : " + location);
        for (int i = 9; i > num - 1; i--) {
            while (nums[i] != 0) {
                if (i == num && location == 0) {
                    count++;
                    nums[i]--;
                    System.out.println((count));
                    answer = count;
                    queue.add(queue.remove());
                    location = queue.size() - 1;
                } else if (location == 0) {
                    queue.add(queue.remove());
                    location = queue.size() - 1;
                } else if (i == queue.peek()) {
                    count++;
                    location--;
                    nums[i]--;
                    queue.remove();
                } else {
                    location--;
                    queue.add(queue.remove());
                }
//                 System.out.println("queue : " + queue + " | count : " + count + " | location : " + location);
            }
        }
        return answer;
    }
}