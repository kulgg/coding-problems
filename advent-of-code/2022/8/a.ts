console.log("hi");

const text = await Deno.readTextFile("input.txt");

const trees = text
  .split("\n")
  .map((x) => x.split("").map((x) => parseInt(x, 10)));
const rows = trees.length;
const cols = trees[0].length;

console.log(trees[rows - 1]);
console.log(rows);
console.log(cols);

const seen: [number, number][] = [];
let num_visible = 0;

function contains(arr: [number, number][], i: number, j: number): boolean {
  return arr.findIndex((x) => x[0] === i && x[1] === j) !== -1;
}

// top
for (let i = 0; i < cols; i++) {
  let max = -1;
  for (let j = 0; j < rows; j++) {
    const oldMax = max;
    max = Math.max(max, trees[j][i]);
    if (contains(seen, j, i)) {
      continue;
    }

    if (trees[j][i] > oldMax) {
      num_visible += 1;
      seen.push([j, i]);
    }
  }
}
// bottom
for (let i = 0; i < cols; i++) {
  let max = -1;
  for (let j = rows - 1; j >= 0; j--) {
    const oldMax = max;
    max = Math.max(max, trees[j][i]);
    if (contains(seen, j, i)) {
      continue;
    }

    if (trees[j][i] > oldMax) {
      num_visible += 1;
      seen.push([j, i]);
    }
  }
}
// left
for (let i = 0; i < rows; i++) {
  let max = -1;
  for (let j = 0; j < cols; j++) {
    const oldMax = max;
    max = Math.max(max, trees[i][j]);
    if (contains(seen, i, j)) {
      continue;
    }

    if (trees[i][j] > oldMax) {
      num_visible += 1;
      seen.push([i, j]);
    }
  }
}
// right
for (let i = 0; i < rows; i++) {
  let max = -1;
  for (let j = cols - 1; j >= 0; j--) {
    const oldMax = max;
    max = Math.max(max, trees[i][j]);
    if (contains(seen, i, j)) {
      continue;
    }

    if (trees[i][j] > oldMax) {
      num_visible += 1;
      seen.push([i, j]);
    }
  }
}

console.log("Visible trees:", num_visible);
