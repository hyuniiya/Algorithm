function solution(array, n) {
    let closest = array[0]; 

    for (let i = 1; i < array.length; i++) {
        const current = array[i];

        const currentDiff = Math.abs(current - n);
        const closestDiff = Math.abs(closest - n);

        if (currentDiff < closestDiff) {
            closest = current;
        } else if (currentDiff === closestDiff && current < closest) {
            closest = current;
        }
    }

    return closest;
}