class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        for(int i = 1; i < numLog.length; i++){
            int gap = numLog[i] - numLog[i-1];
            if(gap == 1){
                answer += 'w';
            }else if(gap == -1){
                answer += 's';
            }else if(gap == 10){
                answer += 'd';
            }else if(gap == -10){
                answer += 'a';
            }
        }
        return answer;
    }
}