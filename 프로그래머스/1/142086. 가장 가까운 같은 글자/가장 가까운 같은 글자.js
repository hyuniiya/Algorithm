function solution(s) {
    const result = new Array(s.length).fill(-1);
    const stack = {}; 

    for (let i = 0; i < s.length; i++) {
        const char = s[i];

        if (stack[char] !== undefined) {
            result[i] = i - stack[char];
        }

        stack[char] = i;
    }

    return result;
}