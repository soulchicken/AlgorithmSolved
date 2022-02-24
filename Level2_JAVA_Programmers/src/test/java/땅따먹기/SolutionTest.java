package 땅따먹기;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        assertEquals(new Solution().solution(new int[][] {{1,2,3,5},{5,6,7,8},{4,3,2,1}}),16);
    }

    @Test
    void findMax() {
        assertEquals(Solution.findMax(new int[] {1,2,3,4}),4);
        assertEquals(Solution.findMax(new int[] {1,8,3,4}),8);
    }
}