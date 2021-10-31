// 근묵자흑

const solution = (J, data) => {
  let n = parseInt(J[0]);
  let k = parseInt(J[1]);
  let cnt = 1;
  n -= k;
  k -= 1;
  cnt += n % k == 0 ? n / k : n / k + 1;
  console.log(parseInt(cnt));
};

// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const data = [];
let N = 0;
let K = 0;
let count = 0;

rl.on("line", function (line) {
  if (N < 1) {
    N = +line;
    K = line.split(" ");
  } else {
    const target = line.split(" ");
    for (let i = 0; i < target.length; i++) {
      data.push(parseInt(target[i]));
    }
    count += 1;
  }
  if (count === 1) {
    rl.close();
  }
}).on("close", function () {
  solution(K, data);
  process.exit();
});
