import java.util.*;
class Solution {
    public int solution(int[] num_list) {
        StringBuilder even = new StringBuilder();
        StringBuilder odd = new StringBuilder();
        for(int num : num_list){
            if(num % 2 == 0){
                even.append(num);
            }
            else{
                odd.append(num);
            }
        }
        int evenNum = Integer.parseInt(even.toString());
        int oddNum = Integer.parseInt(odd.toString());
        
        return evenNum + oddNum;
    }
}