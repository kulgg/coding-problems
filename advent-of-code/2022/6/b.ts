const text = await Deno.readTextFile("input.txt");
console.log("text", text);

const four: string[] = [];
let result = 0;

for (let i = 0; i < text.length; i++) {
  four.push(text[i]);
  const set = new Set(four);
  console.log(set);
  if (set.size === 14) {
    result = i + 1;
    break;
  }
  if (i >= 13) {
    four.shift();
  }
}

console.log("result", result);
