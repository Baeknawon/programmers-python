import java.util.Arrays;
class Solution {
    public String[] solution(String my_string) {
        int length = my_string.length();
        String[] suffixes = new String[length];
        
        //접미사 생성
        for(int i = 0; i < length; i++){
            suffixes[i] = my_string.substring(i);
        }
        //사전배열
        Arrays.sort(suffixes);
        
        return suffixes;
    }
}