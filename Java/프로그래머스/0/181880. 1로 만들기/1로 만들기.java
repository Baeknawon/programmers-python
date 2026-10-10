class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for(int n : num_list){
            answer += (int) Math.floor(Math.log(n) / Math.log(2));
        }
        return answer;
    }
}