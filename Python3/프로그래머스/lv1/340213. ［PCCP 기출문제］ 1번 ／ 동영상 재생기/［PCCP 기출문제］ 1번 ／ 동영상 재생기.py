def solution(video_len, pos, op_start, op_end, commands):
    #문자열 초변환
    video_len = int(video_len[:2]) * 60 + int(video_len[3:])
    pos = int(pos[:2]) * 60 + int(pos[3:])
    op_start = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end = int(op_end[:2]) * 60 + int(op_end[3:])
    for i in range(len(commands)):
        if op_start <= pos <= op_end:
            pos = op_end
            
        if commands[i] == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
            
        if commands[i] == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
                
        if op_start <= pos <= op_end:
            pos = op_end   
    #다시 초에서 문자열 변환
    m = pos // 60
    s = pos % 60
    answer = f"{m:02d}:{s:02d}"
    
                
    
    return answer