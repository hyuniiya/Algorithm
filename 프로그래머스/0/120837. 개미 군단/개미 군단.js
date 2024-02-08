function solution(hp) {
    let b_ant = Math.floor(hp / 5);
    const g_ant = Math.floor((hp % 5) / 3)
    const w_ant = (hp % 5) % 3
    return b_ant + g_ant + w_ant
}