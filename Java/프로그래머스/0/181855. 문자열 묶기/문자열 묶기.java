import java.util.*;
class Solution {
    public int solution(String[] strArr) {
        int[] answer = new int[31];
        for(String str : strArr){
            int num = str.length();
            answer[num]++;
        }
        Arrays.sort(answer);
        return answer[30];
    }
}