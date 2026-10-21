import java.util.*;
class Solution {
    public int solution(int[] arr) {
        int n = 0;
        while(true){
            int[] prev = Arrays.copyOf(arr, arr.length); //변환 전 상태 저장
            for(int i = 0; i< arr.length; i++){
                if(arr[i] >= 50 && arr[i] % 2 == 0){
                    arr[i] /= 2;
                }
                else if(arr[i] < 50 && arr[i] % 2 != 0){
                    arr[i] = arr[i] * 2 + 1;
                }
            }
            
            if(Arrays.equals(arr,prev)){
                break;
            }
            n++;
        }
        return n;
    }
}