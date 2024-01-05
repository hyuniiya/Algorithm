function solution(babbling) {
    var answer = 0;
    var word = "";
    var str = ["aya", "ye", "woo", "ma"];
    
    for(var i=0; i<babbling.length; i++) {
        word = babbling[i].toString();

        for(var j=0; j<str.length; j++) {
            word = word.replaceAll(str[j], ' ');    
        }


        if( word.trim().length == 0) {
            answer++;
        }

    }
    return answer;
}