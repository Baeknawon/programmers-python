import java.util.*;
class Solution {
    public String[] solution(String[] strArr) {
        String[] arr = new String[strArr.length];
        int j = 0;
        
        for(int i = 0; i < strArr.length; i++){
            if(!strArr[i].contains("ad")){
                arr[j++] = strArr[i];
            }
        }
        return Arrays.copyOf(arr, j); //arr 배열을 길이만큼 복사..
    }
}