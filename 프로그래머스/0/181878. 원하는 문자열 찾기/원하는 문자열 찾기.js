function solution(myString, pat) {
    myString = myString.toLowerCase();
    pat = pat.toLowerCase();

    for (let i = 0; i <= myString.length - pat.length; i++) {
        if (myString.substring(i, i + pat.length) === pat) {
            return 1;
        }
    }
    return 0;
}