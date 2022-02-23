package 다리를_지나는_트럭;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void test_1() {
        assertEquals(new Solution().solution(2,10, new int[] {7,4,5,6}),8);
    }
    @Test
    void test_2() {
        assertEquals(new Solution().solution(100,100,new int[] {10}),101);
    }
    @Test
    void test_3() {
        assertEquals(new Solution().solution(100,100,new int[] {10,10,10,10,10,10,10,10,10,10}),110);
    }
}