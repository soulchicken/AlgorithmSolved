package 주식가격;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        assertEquals(Arrays.toString((new Solution().solution(new int[]{1, 2, 3, 2, 3}))),"[4, 3, 1, 1, 0]");
    }
}