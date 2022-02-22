package 피보나치수;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        Solution solution = new Solution();
        assertEquals(solution.solution(3),2);
        assertEquals(solution.solution(5),5);
    }
}