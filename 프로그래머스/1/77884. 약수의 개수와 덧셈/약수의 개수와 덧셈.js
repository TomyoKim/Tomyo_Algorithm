function solution(left, right) {
    let answer = 0;
    for(let i = left; i <= right; i++){
        let count = 0;
        for(let j = 1; j <= i; j++){
            if(i % j === 0){
                count += 1
            }
            if(i === j){
                if(count % 2 === 0){
                    answer += i;
                } 
                else {
                    answer -= i;
                }
            }
        }
    }
    return answer;
}