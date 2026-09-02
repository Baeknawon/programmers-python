class Solution {
    public int solution(int[] num_list) {
        int answer = 1;
        int n = num_list.length;
        if(n <= 10){
            for(int i : num_list){
                answer *= i;
            }
        }else{
            for(int i : num_list){
                answer += i;
            }
            answer -= 1;
        }
        return answer;
    }
}