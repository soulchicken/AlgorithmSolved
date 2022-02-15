public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution("1S2D*3T"));
        System.out.println(s.solution("1D2S#10S"));
        System.out.println(s.solution("1D2S0T"));
        System.out.println(s.solution("1S*2T*3S"));
        System.out.println(s.solution("1D#2S*3S"));
        System.out.println(s.solution("1T2D3D#"));
        System.out.println(s.solution("1D2S3T*"));
    }
}