class Solution {
    public int solution(int a, int b) {
        
        String C = a + "" + b;
        int c = Integer.parseInt(C);
        int d = 2 * b * a;
        if(c >= d){
            return c;
        }else{
            return d;
        }
    
    }
}