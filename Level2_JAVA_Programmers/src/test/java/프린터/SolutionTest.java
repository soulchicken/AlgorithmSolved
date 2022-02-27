package 프린터;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        assertEquals(new Solution().solution(new int[] {2,1,3,2}, 2),1);
    }
    @Test
    void solution2() {
        assertEquals(new Solution().solution(new int[] {1,1,9,1,1,1}, 0),5);
    }

    @Test
    void solution3() {
        assertEquals(new Solution().solution(new int[] {1, 9, 1, 9, 1, 9}, 0),4);
    }
}