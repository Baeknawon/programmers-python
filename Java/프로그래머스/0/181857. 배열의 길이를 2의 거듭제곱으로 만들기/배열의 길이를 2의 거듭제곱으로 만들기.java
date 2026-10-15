import java.util.*;
class Solution {
    public List solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        for(int x : arr){
            answer.add(x);
        }
        for(;;){
            int n = answer.size();
            double indi = Math.log(n) / Math.log(2);
            if(indi % 1 == 0){
                break;
            }
            else{
                answer.add(0);
            }
            
        }
        
        return answer;
    }
}