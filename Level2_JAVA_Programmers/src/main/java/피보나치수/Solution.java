package 피보나치수;

import java.util.ArrayList;

class Solution {
    public int solution(int n) {
        ArrayList<Integer> fibo = new ArrayList<>();
        fibo.add(0);
        fibo.add(1);
        for (int i = 2; i < n+1; i++) {
            fibo.add((fibo.get(i-1) + fibo.get(i-2))%1234567);
        }
        return fibo.get(n);
    }
}