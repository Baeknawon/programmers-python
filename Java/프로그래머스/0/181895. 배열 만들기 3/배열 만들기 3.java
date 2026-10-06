import java.util.*;
class Solution {
    public List solution(int[] arr, int[][] intervals) {
        List<Integer> answer = new ArrayList<>();
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < arr.length; j++){
                if(j >= intervals[i][0] && j <= intervals[i][1]){
                    answer.add(arr[j]);
                }
            }
        }
        return answer;
    }
}