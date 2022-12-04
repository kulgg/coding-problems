console.log("hi");
const text = await Deno.readTextFile("input.txt");

const pairs = text.split("\n");

let total = 0;
pairs.forEach((pair) => {
  const [[x1, x2], [y1, y2]] = pair
    .split(",")
    .map((x) => x.split("-").map((y) => parseInt(y, 10)));

  if (x2 >= y1 && x2 <= y2) {
    total += 1;
  } else if (y2 >= x1 && y2 <= x2) {
    total += 1;
  }
});

console.log("Result", total);
