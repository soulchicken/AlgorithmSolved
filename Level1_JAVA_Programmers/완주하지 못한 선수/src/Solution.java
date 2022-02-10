import java.util.Arrays;
import java.util.Objects;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        for (int i = 0; i < completion.length; i++) {
            if (!Objects.equals(completion[i], participant[i])) {
                return participant[i];
            }
        }
        return participant[participant.length-1];
    }
}