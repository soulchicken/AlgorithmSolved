import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, Integer> index = new HashMap<>();
        Map<String, List<Integer>> li = new HashMap<>();

        for(int i=0 ; i<id_list.length ; i++) {
            index.put(id_list[i],i);
        }

        for(String repo : report) {
            String[] id = repo.split(" ");
            if(!li.containsKey(id[1])) {
                li.put(id[1], new ArrayList<>());
            }
            if(!li.get(id[1]).contains(index.get(id[0]))) {
                li.get(id[1]).add(index.get(id[0]));
            }
        }

        for(int i = 0 ; i < id_list.length ; i++) {
            if(li.containsKey(id_list[i]) && li.get(id_list[i]).size() >= k) {
                for(int idx : li.get(id_list[i])) {
                    answer[idx]++;
                }
            }
        }
        return answer;
    }
}
