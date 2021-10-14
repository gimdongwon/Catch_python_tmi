// 문제 선정하기

const solution = (N, data) => {
  data.sort();
  const target = new Set(data);

  if (target.size >= 3) {
    console.log("YES");
  } else {
    console.log("NO");
  }
};

const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = 0;
  let count = 0;
  const data = [];

  for await (const line of rl) {
    if (N < 1) {
      N = +line;
    } else {
      const target = line.split(" ");
      for (let i = 0; i < target.length; i++) {
        data.push(target[i]);
      }
      // data.push(line);
      // data.push(line.split(' ').map((el) => +el));
      // data.push(line.split('').map((el) => el));
      // data.push(line.split('').map((el) => +el));
      count += 1;
    }
    if (1 === count) {
      rl.close();
    }
  }

  solution(N, data);
  process.exit();
})();
