import java.util.*;
class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int[] top = new int[3];
        int cnt = 0;
        for(int ranking = 1; ranking <= rank.length; ranking++){
            for(int i = 0; i < rank.length; i++){
                if(rank[i] == ranking && attendance[i]){
                    top[cnt++] = i;
                    
                    if(cnt == 3){
                        return 10000 * top[0] + 100 * top[1] + top[2];
                    }
                }
            }
        }
        return 0;
    }
}