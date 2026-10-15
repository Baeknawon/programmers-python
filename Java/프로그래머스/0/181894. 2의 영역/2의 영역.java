import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();
        for(int n : arr){
            list.add(n);
        }
        int first = list.indexOf(2);
        int last = list.lastIndexOf(2);
        if(first == -1){
            answer.add(-1);
        }else{
            answer = list.subList(first,last + 1);
        }
        
        int[] ans = answer.stream().mapToInt(Integer::intValue).toArray();
        return ans;
    }
}