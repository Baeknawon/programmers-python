class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = my_string;
        for(int i = 0; i < queries.length; i++){
            int s = queries[i][0];
            int e = queries[i][1];
            
            StringBuilder reverse = new StringBuilder(answer.substring(s,e+1));
            reverse.reverse();
            if(s == 0){
                answer = reverse + answer.substring(e+1);
            }else{
                answer = answer.substring(0,s) + reverse + answer.substring(e+1);
            }
            
        }
        return answer;
    }
}