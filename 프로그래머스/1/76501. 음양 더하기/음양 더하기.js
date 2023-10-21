function solution(absolutes, signs) {
    let result = 0;
    absolutes.map((value, index) => signs[index] ? result += value : result -= value);
    return result
}