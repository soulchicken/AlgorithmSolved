import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void solution() {
        assertEquals(Solution.solution("...!@BaT#*..y.abcdefghijklm"),"bat.y.abcdefghi");
        assertEquals(Solution.solution("z-+.^."),"z--");
        assertEquals(Solution.solution("=.="),"aaa");
        assertEquals(Solution.solution("123_.def"),"123_.def");
        assertEquals(Solution.solution("abcdefghijklmn.p"),"abcdefghijklmn");
    }

    @Test
    void step1() {
        assertEquals(Solution.step1("...!@BaT#*..y.abcdefghijklm"),"...!@bat#*..y.abcdefghijklm");
        assertEquals(Solution.step1("z-+.^."),"z-+.^.");
        assertEquals(Solution.step1("=.="),"=.=");
        assertEquals(Solution.step1("123_.def"),"123_.def");
        assertEquals(Solution.step1("abcdefghijklmn.p"),"abcdefghijklmn.p");
    }

    @Test
    void step2() {
        assertEquals(Solution.step2("...!@bat#*..y.abcdefghijklm"),"...bat..y.abcdefghijklm");
        assertEquals(Solution.step2("z-+.^."),"z-..");
        assertEquals(Solution.step2("=.="),".");
        assertEquals(Solution.step2("123_.def"),"123_.def");
        assertEquals(Solution.step2("abcdefghijklmn.p"),"abcdefghijklmn.p");
    }

    @Test
    void step3() {
        assertEquals(Solution.step3(".."),".");
        assertEquals(Solution.step3("..1"),".1");
        assertEquals(Solution.step3("1..1"),"1.1");
        assertEquals(Solution.step3("...bat..y.abcdefghijklm"),".bat.y.abcdefghijklm");
        assertEquals(Solution.step3("z-.."),"z-.");
        assertEquals(Solution.step3("."),".");
        assertEquals(Solution.step3("123_.def"),"123_.def");
        assertEquals(Solution.step3("abcdefghijklmn.p"),"abcdefghijklmn.p");
    }

    @Test
    void step4() {
        assertEquals(Solution.step4(".bat.y.abcdefghijklm"),"bat.y.abcdefghijklm");
        assertEquals(Solution.step4("z-."),"z-");
        assertEquals(Solution.step4("."),"");
        assertEquals(Solution.step4("123_.def"),"123_.def");
        assertEquals(Solution.step4("abcdefghijklmn.p"),"abcdefghijklmn.p");
    }

    @Test
    void step5() {
        assertEquals(Solution.step5("bat.y.abcdefghijklm"),"bat.y.abcdefghijklm");
        assertEquals(Solution.step5("z-"),"z-");
        assertEquals(Solution.step5(""),"a");
        assertEquals(Solution.step5("123_.def"),"123_.def");
        assertEquals(Solution.step5("abcdefghijklmn.p"),"abcdefghijklmn.p");
    }

    @Test
    void step6() {
    }

    @Test
    void step7() {
    }
}