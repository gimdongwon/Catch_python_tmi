function solution(block, board) {
  if (block === 0 || block === 4 || block === 5) {
    return 2;
  } else {
    return 1;
  }
  let startRow = 0;
  let startColumn = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (block === 0 && board[i][j] === 0) {
        startRow = i;
        startColumn = j;
      }
    }
  }
}

// 상자 배치후 꽉찬 줄은 터뜨림

function check_block(board) {
  let result = 0;
  for (let i = 0; i < board.length; i++) {
    let row = 0;
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] == 0) {
        row++;
      }
    }
    if (row === board[i].length) {
      result += 1;
    }
  }
  return result;
}
