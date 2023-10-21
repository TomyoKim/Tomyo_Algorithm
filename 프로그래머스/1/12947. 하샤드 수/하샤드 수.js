function solution(x) {
    let num = String(x).split('').map(a => Number(a)).reduce((arr, cur) => arr + cur);
    return (x % num) ? false : true;
}