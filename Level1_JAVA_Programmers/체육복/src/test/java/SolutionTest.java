import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solutionTest() {
        assertEquals(new Solution().solution(5,new int[] {2,4}, new int[] {1,3,5}),5);
        assertEquals(new Solution().solution(5,new int[] {2,4}, new int[] {3}),4);
        assertEquals(new Solution().solution(3,new int[] {3}, new int[] {1}),2);
    }
}