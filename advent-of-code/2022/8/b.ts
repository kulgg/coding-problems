console.log("hi");
const text = await Deno.readTextFile("input.txt");

const trees = text
  .split("\n")
  .map((x) => x.split("").map((x) => parseInt(x, 10)));
const rows = trees.length;
const cols = trees[0].length;

console.log(rows);
console.log(cols);

let best = 0;

for (let i = 0; i < rows; i++) {
  for (let j = 0; j < cols; j++) {
    let score = 1;
    const height = trees[i][j];

    let tmp = 0;
    for (let k = j + 1; k < cols; k++) {
      if (trees[i][k] < height) {
        tmp += 1;
      } else {
        tmp += 1;
        break;
      }
    }
    score *= tmp;
    tmp = 0;
    for (let k = j - 1; k >= 0; k--) {
      if (trees[i][k] < height) {
        tmp += 1;
      } else {
        tmp += 1;
        break;
      }
    }
    score *= tmp;
    tmp = 0;
    for (let k = i + 1; k < rows; k++) {
      if (trees[k][j] < height) {
        tmp += 1;
      } else {
        tmp += 1;
        break;
      }
    }
    score *= tmp;
    tmp = 0;
    for (let k = i - 1; k >= 0; k--) {
      if (trees[k][j] < height) {
        tmp += 1;
      } else {
        tmp += 1;
        break;
      }
    }
    score *= tmp;

    best = Math.max(best, score);
  }
}

console.log("best scenic:", best);
