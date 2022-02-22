package 최솟값만들기;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        Solution s = new Solution();
        assertEquals(s.solution(new int[] {1, 4, 2}, new int[] {5, 4, 4}),29);
        assertEquals(s.solution(new int[] {1, 2}, new int[] {3, 4}),10);
    }
}