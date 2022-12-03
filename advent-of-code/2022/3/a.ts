const input = await Deno.readTextFile("./input.txt");

const lines = input.split("\n");

let items = "";

for (const line of lines) {
  const len = line.length;
  const middle = Math.floor(len / 2);
  const first = line.slice(0, middle);
  const second = line.slice(middle, len);
  for (const c of first) {
    if (second.indexOf(c) > -1) {
      items += c;
      break;
    }
  }
}

console.log(items);

let total = 0;

for (let i = 0; i < items.length; i++) {
  const ascii = items.charCodeAt(i);
  total += ascii > 90 ? ascii - 96 : ascii - 38;
}

console.log(total);
