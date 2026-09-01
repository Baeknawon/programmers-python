class Solution {
    public int[] solution(String myString) {
        String[] s = myString.split("x", -1); // -1은 구분자를 기준으로 구분할 떄, 빈 문자열까지 포함하여 반환한다
        int[] answer = new int[s.length];
        for(int i = 0; i<s.length; i++){
            answer[i]  = s[i].length();
        }
        return answer;
    }
}