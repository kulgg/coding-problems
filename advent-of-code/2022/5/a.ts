console.log("Hi");

const text = await Deno.readTextFile("input.txt");

const [stacks_input, instructions] = text.split("\n\n");
const lines = stacks_input.split("\n");
const stacks_num = Math.floor((lines[0].length + 1) / 4);
const stacks: string[][] = [];

for (let i = 0; i < stacks_num; i++) {
  stacks.push([]);
}

console.log("stacks", stacks);

for (let j = lines.length - 2; j >= 0; j--) {
  for (let i = 0; i < stacks_num; i++) {
    const index = i * 4 + 1;
    if (lines[j][index] !== " ") {
      stacks[i].push(lines[j][index]);
    }
  }
}

console.log("stacks", stacks);

const instructions_lines = instructions.split("\n");

for (const instr of instructions_lines) {
  const segments = instr.split(" ");
  const amount = parseInt(segments[1]);
  const fromIndex = parseInt(segments[3]) - 1;
  const toIndex = parseInt(segments[5]) - 1;

  for (let i = 0; i < amount; i++) {
    stacks[toIndex].push(stacks[fromIndex].pop()!);
  }
}

console.log(stacks.map((x) => x.pop()).join(""));
