class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        
        boolean one = x1 || x2;
        boolean two = x3 || x4;
        boolean answer = one && two;
        return answer;
    }
}