package 전화번호_목록;

import java.util.Arrays;

public class Solution {
    public boolean solution(String[] phone_book) {
        if (phone_book.length == 1) {
            return true;
        }
        Arrays.sort(phone_book);
        int a;
        int b;
        for (int i = 0; i < phone_book.length - 1; i++) {
            a = phone_book[i].length();
            b = phone_book[i+1].length();
//            System.out.println(phone_book[i] + " : "+ a);
//            System.out.println(phone_book[i+1] + " : "+ b);
//            System.out.println();
            if (a > b && phone_book[i].substring(0, b).equals(phone_book[i + 1])) {
//                System.out.println("a > b인 상태");
//                System.out.println(phone_book[i+1]);
//                System.out.println(phone_book[i].substring(0,b));
                return false;
            } else if (b > a && phone_book[i + 1].substring(0, a).equals(phone_book[i])) {
//                System.out.println("a < b인 상태");
//                System.out.println(phone_book[i]);
//                System.out.println(phone_book[i].substring(0,a));
                return false;
            }
        }
        return true;
    }
}