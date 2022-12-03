const input = await Deno.readTextFile("./input.txt");

const lines = input.split("\n");

let items = "";

for (let i = 0; i < lines.length; i += 3) {
  const first = lines[i];
  const second = lines[i + 1];
  const third = lines[i + 2];

  for (const c of first) {
    if (second.indexOf(c) > -1 && third.indexOf(c) > -1) {
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
