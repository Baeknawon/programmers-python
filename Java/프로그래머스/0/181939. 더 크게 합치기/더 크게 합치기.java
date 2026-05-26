class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String A = Integer.toString(a); //문자열로 반환
        String B = Integer.toString(b);
        String C = A + "" + B;
        String D = B + "" + A;
        int c = Integer.parseInt(C);
        int d = Integer.parseInt(D);
        if(c >= d){
            answer = c;
        }else{
            answer = d;
        }
        return answer;
    }
}