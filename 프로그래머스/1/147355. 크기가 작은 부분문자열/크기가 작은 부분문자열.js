function solution(t, p) {
    let numberP = Number(p);
    let ans = 0;
    for(let i = 0; i < t.length - p.length + 1; i++){
        let slicedT = t.slice(i, i + p.length);
        let numberT = Number(slicedT);
        
        if(numberT <= numberP){
            ans += 1;
        }
    }
    
    return ans;
}