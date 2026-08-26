import java.util.*;
class Solution {
    public String[] solution(String myString) {
        String[] splitArr = myString.split("x");
        //빈문자열 제외해야됨
        String[] answer = Arrays.stream(splitArr).filter(s -> !s.isEmpty()).toArray(String[]::new);
        
        Arrays.sort(answer);
        return answer;
    }
}