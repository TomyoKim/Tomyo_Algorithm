function solution(s) {
    let result = [];
    for(let i = 0; i < s.length; i++) {
        let distance = 0;
        for(let j = i - 1; j >= 0; j--) {
            if(s[i] === s[j]) {
                distance = i - j;
                break;
            }
        }
        if(distance !== 0) {
            result[i] = distance;
        } else {
            result[i] = -1;
        }
    }
    
    return result;
}