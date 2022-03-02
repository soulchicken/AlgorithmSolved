package 전화번호_목록;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        assertFalse(new Solution().solution(new String[]{"119", "97674223", "1195524421"}));
    }

    @Test
    void solution1() {
        assertTrue(new Solution().solution(new String[]{"123","456","789"}));
    }

    @Test
    void solution2() {
        assertFalse(new Solution().solution(new String[]{"12","123","1235","567","88"}));
    }
}