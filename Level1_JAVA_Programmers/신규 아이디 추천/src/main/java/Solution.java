public class Solution {
    public static void main(String[] args) {
        solution("...!@BaT#*..y.abcdefghijklm");
    }

    public static String solution(String new_id) {
        String id = step1(new_id);
        id = step2(id);
        id = step3(id);
        id = step456(id);
        id = step7(id);
        return id;
    }

    //1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    public static String step1(String id) {
        return id.toLowerCase();
    }

    //2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    public static String step2(String id) {
        String step2 = "";
        char a;
        for (int i = 0; i < id.length(); i++) {
            a = id.charAt(i);
            if (Character.isDigit(a) || Character.isLowerCase(a) || a == '-'
                 || a == '_' || a == '.') {
                step2 += a;
            }
        }
        return step2;
    }

    //3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    // 정규표현식이 필요했음
    public static String step3(String id) {
        while (id.contains("..")) {
            id = id.replaceFirst("\\.\\.",".");
        }
        return id;
    }

    private static String step456(String id) {
        do {
            id = step4(id);
            id = step5(id);
            id = step6(id);
        }while(id.charAt(0) == '.' || id.charAt(id.length()-1) == '.');
        return id;
    }

    //4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    public static String step4(String id) {
        if (id.charAt(0) == '.') {
            id = id.substring(1);
        }
        if (id.length() != 0 && id.charAt(id.length()-1) == '.') {
            id = id.substring(0,id.length()-1);
        }
        return id;
    }

    //5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    public static String step5(String id) {
        if (id.length() == 0) {
            id = "a";
        }
        return id;
    }

    //6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    //만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    public static String step6(String id) {
        if (id.length() > 15) {
            id = id.substring(0,15);
        }
        return id;
    }

    //7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    public static String step7(String id) {
        while (id.length() < 3) {
            id += id.charAt(id.length()-1);
        }
        return id;
    }
}