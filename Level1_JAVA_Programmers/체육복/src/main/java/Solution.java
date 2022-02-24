import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        HashSet<Integer> lostPeople = new HashSet<>();
        HashSet<Integer> lostPeople2 = new HashSet<>();
        HashSet<Integer> reservePeople = new HashSet<>();

        for (int i : lost) {
            lostPeople.add(i);
            lostPeople2.add(i);
        }
        for (int j : reserve) {
            reservePeople.add(j);
        }

        lostPeople.removeAll(reservePeople);
        reservePeople.removeAll(lostPeople2);

        ArrayList<Integer> realReserve = new ArrayList<>();
        Iterator<Integer> iter = reservePeople.iterator();
        while (iter.hasNext()) {
            realReserve.add(iter.next());
        }
        Collections.sort(realReserve);

        ArrayList<Integer> realLost = new ArrayList<>();
        iter = lostPeople.iterator();
        while (iter.hasNext()) {
            realLost.add(iter.next());
        }
        Collections.sort(realLost);

        int real = realLost.size();
        int i = 0;
        while (i < realLost.size()) {
            for (int j = 0; j < realReserve.size(); j++) {
                if (realLost.get(i) == realReserve.get(j) - 1) {
                    realLost.remove(i);
                    realReserve.remove(j);
                    i--;
                    break;
                } else if (realLost.get(i) == realReserve.get(j) + 1) {
                    realLost.remove(i);
                    realReserve.remove(j);
                    i--;
                    break;
                }
            }
            i++;
        }
        return answer - realLost.size();
    }
}