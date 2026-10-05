class Solution {
    public int solution(int[] num_list) {
        int odd = 0;
        int even = 0;
        for(int i = 0; i< num_list.length; i++){
            if((i+2) % 2 == 0){ //이러면 홀수번째
                odd += num_list[i];
            }
            else{
                even += num_list[i];
            }
        }
        int answer = Math.max(odd,even);
        
        return answer;
    }
}