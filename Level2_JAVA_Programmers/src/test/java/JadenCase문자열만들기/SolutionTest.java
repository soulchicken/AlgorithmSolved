package JadenCase문자열만들기;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        Solution solution = new Solution();
        assertEquals(solution.solution("3people unFollowed me"),"3people Unfollowed Me");
        assertEquals(solution.solution("for the last week"),"For The Last Week");
    }

    @Test
    void makeJaden() {
        Solution solution = new Solution();
        assertEquals(solution.makeJaden("3people"),"3people");
        assertEquals(solution.makeJaden("unFollowed"),"Unfollowed");
        assertEquals(solution.makeJaden("me"),"Me");
        assertEquals(solution.makeJaden("for"),"For");
        assertEquals(solution.makeJaden("the"),"The");
        assertEquals(solution.makeJaden("last"),"Last");
        assertEquals(solution.makeJaden("week"),"Week");
    }
}