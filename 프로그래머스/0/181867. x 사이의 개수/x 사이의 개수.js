function solution(myString) {
    let lengths = [];
    let currentLength = 0;

    for (let i = 0; i < myString.length; i++) {
        if (myString[i] === 'x') {
            lengths.push(currentLength);
            currentLength = 0;
        } else {
            currentLength++;
        }
    }

    lengths.push(currentLength);

    return lengths;
}