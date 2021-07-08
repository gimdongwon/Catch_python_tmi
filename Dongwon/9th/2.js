function solution(money, cost) {
  let zero_list = [];
  let result = [];
  let max_length = 0;
  let change_cost = {};
  for (let i = 0; i < cost.length; i++) {
    change_cost[i] = cost[i];
    if (cost[i] == 0) {
      zero_list.push(i);
    }
  }
  let a = Object.entries(change_cost);
  let target = a.filter((item) => item[1] !== 0);
  for (let i = target.length; i > 0; i--) {
    let b = combinations(target, i);
    for (let j = 0; j < b.length; j++) {
      let temp_money = money;
      let temp_list = [];
      for (let k = 0; k < b[j].length; k++) {
        if (b[j][k][1] <= temp_money) {
          temp_money -= b[j][k][1];
          temp_list.push(b[j][k]);
        } else {
          break;
        }
      }
      if (temp_list.length) {
        let answer = [];
        for (let i = 0; i < temp_list.length; i++) {
          answer.push(parseInt(temp_list[i][0]));
        }
        for (let i = 0; i < zero_list.length; i++) {
          answer.push(zero_list[i]);
        }
        answer.sort();
        result.push(check_continuty(answer));
      }
    }
  }
  return result.length ? Math.max.apply(null, result) : 0;
}

// 연속된 경우의 수를 구하기 위한 combination 함수

const combinations = (arr, m) => {
  const result = [];
  const picked = [];
  const used = [];
  for (let item of arr) used.push(0);

  function find(picked) {
    if (picked.length === m) {
      const rst = [];
      for (let i of picked) {
        rst.push(arr[i]);
      }
      result.push(rst);
    } else {
      let start = picked.length ? picked[picked.length - 1] + 1 : 0;
      for (let i = start; i < arr.length; i++) {
        if (i === 0 || arr[i] !== arr[i - 1] || used[i - 1]) {
          picked.push(i);
          used[i] = 1;
          find(picked);
          picked.pop();
          used[i] = 0;
        }
      }
    }
  }
  find(picked);
  return result;
};

// 연속된 층을 세는 함수

function check_continuty(arr) {
  let result = 0;
  let temp = 1;
  let i = 0;
  let maxNum = Math.max.apply(null, arr);
  while (i < arr.length) {
    if (arr[i + 1] - arr[i] === 1) {
      temp += 1;
    } else {
      result = Math.max(result, temp);
    }
    i++;
  }
  return result;
}

/*

누적 합

*/