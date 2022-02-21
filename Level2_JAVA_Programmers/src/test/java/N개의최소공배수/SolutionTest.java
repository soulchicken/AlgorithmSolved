package N개의최소공배수;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solutionTest() {
        Solution solution = new Solution();
        assertEquals(solution.solution(new int[] {2,6,8,14}),168);
        assertEquals(solution.solution(new int[] {1,2,3}),6);
    }

    @Test
    void makeLCMTest() {
        Solution solution = new Solution();
        assertEquals(solution.makeLCM(1,3),3);
        assertEquals(solution.makeLCM(2,3),6);
        assertEquals(solution.makeLCM(8,14),56);
    }
}