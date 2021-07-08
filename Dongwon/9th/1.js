function solution(k, rates) {
  // 다음 값이 현재 값보다 비싸면 안파는 로직
  let money = k;
  let dollar = 0;
  for (let i = 0; i < rates.length; i++) {
    // 달러 사기
    if (money >= rates[i] && i < rates.length - 1) {
      // 달러가 다음 값보다 쌀때 사기
      if (rates[i] < rates[i + 1]) {
        dollar += 1;
        money -= rates[i];
      }
      // 안싸면 안사기
      else {
        continue;
      }
    }
    // 달러 팔기
    else if (dollar === 1 && i < rates.length - 1) {
      if (rates[i] > rates[i + 1]) {
        dollar -= 1;
        money += rates[i];
      }
      // 달러 다음 값보다 쌀때 안팔기
      else {
        continue;
      }
    }
    if (i === rates.length - 1 && dollar == 1) {
      dollar -= 1;
      money += rates[i];
    }
  }
  return money;
}
