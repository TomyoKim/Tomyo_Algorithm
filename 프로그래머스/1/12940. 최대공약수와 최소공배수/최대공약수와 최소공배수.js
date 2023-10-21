function solution(n, m) {
    const minN = Math.min(n, m);
    const maxN = Math.max(n, m);

    function gcd(a, b){
        return a % b === 0 ? b : gcd(b, a % b);
    }
    
    function lcm(a, b){
        return a * b / gcd(a, b)
    }

  return [gcd(maxN, minN), lcm(maxN, minN)];
}