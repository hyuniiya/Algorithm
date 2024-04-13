function solution(n) {
    const desc = String(n)
                  .split('')
                  .sort()
                  .reverse()
                  .join('');
    return parseInt(desc, 10);
}