// 사은품 교환하기

const solution = (data) => {
  let n = parseInt(data[0]),
    m = parseInt(data[1]);

  console.log(parseInt(Math.min((n + m) / 12, n / 5)));
};

// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const data = [];
let N = 0;
let count = 0;

rl.on("line", function (line) {
  if (N < 1) {
    N = +line;
  } else {
    const arr = line.split(" ");
    solution(arr);
    count += 1;
  }
  if (count === N) {
    rl.close();
  }
}).on("close", function () {
  // solution(N, data)
  process.exit();
});
