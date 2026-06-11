class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        char[] ms = my_string.toCharArray();
        int s = my_string.length() - n;
        for(int i = s; i < my_string.length(); i++){
            answer += ms[i];
        }
        return answer;
    }
}