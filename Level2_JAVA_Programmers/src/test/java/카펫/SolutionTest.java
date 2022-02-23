package 카펫;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        assertArrayEquals(new Solution().solution(10,2),new int[] {4,3});
        assertArrayEquals(new Solution().solution(8,1),new int[] {3,3});
        assertArrayEquals(new Solution().solution(24,24),new int[] {8,6});
    }
}