function solution(my_string) {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    
    const resultArray = my_string.split('').filter(i => !vowels.includes(i));
    return resultArray.join('');
}