function solution(s) {
    let n = Math.floor(s.length / 2);
    return s.length % 2 ? s.substr(n, 1) : s.substr(n-1, 2);
}