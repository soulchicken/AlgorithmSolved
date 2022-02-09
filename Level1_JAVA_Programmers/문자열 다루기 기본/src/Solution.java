class Solution {
    public boolean solution(String s) {
        try {
            Integer.parseInt(s);
            if (s.length() == 4 || s.length() == 6) {
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            return false;
        }
    }
}