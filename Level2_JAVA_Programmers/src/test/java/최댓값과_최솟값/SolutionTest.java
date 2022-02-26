package 최댓값과_최솟값;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        assertEquals(new Solution().solution("1 2 3 4"),"1 4");
        assertEquals(new Solution().solution("-1 -2 -3 -4"),"-4 -1");
        assertEquals(new Solution().solution("-1 -1"),"-1 -1");
    }
}