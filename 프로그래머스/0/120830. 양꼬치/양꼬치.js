function solution(n, k) {
    const serviceDrinks = Math.floor(n / 10);
    const totalPayment = (n * 12000) + (k * 2000 - serviceDrinks * 2000);
    return totalPayment;
}