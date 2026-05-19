import java.util.*;
class Solution {
    public List solution(int l, int r) {
        List<Integer> answer = new ArrayList<>();
        for(int i = l; i<=r; i++){
            String s = i+""; //가장 끝 인덱스를 공백으로 둬야 마지막 숫자까지 확인 가능
            boolean bool = true;
            for(char c : s.toCharArray()){//문자열을 배열로 만들어서 반복
                if(c != '5' && c != '0'){
                    bool = false;
                }
            }
            if(bool){
                answer.add(i);
            }
        }
        if(answer.isEmpty()){
            answer.add(-1);
        }
            
        return answer;
    }
}