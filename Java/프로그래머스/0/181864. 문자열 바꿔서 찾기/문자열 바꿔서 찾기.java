class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String rpString = myString.replace('A', 'O').replace('B', 'A').replace('O', 'B');
        if(rpString.contains(pat)){
            answer = 1;
        }
        return answer;
    }
}