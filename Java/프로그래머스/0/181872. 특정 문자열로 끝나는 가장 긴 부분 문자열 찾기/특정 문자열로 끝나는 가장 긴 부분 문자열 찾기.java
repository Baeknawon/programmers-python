class Solution {
    public String solution(String myString, String pat) {
        int last = myString.lastIndexOf(pat);
        String answer = myString.substring(0, last + pat.length());
        return answer;
    }
}