function solution(s, n) {
  return s.split('').map(a => {
      if(a === ' '){
          return a;
      }
      const numCode = a.charCodeAt();
      return a.toUpperCase().charCodeAt() + n > 90 
          ? String.fromCharCode(numCode - 26 + n)
          : String.fromCharCode(numCode + n)
  }).join('')
}