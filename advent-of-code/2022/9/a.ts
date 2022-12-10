console.log("hi");

const text = await Deno.readTextFile("input.txt");

const moves = text.split("\n");

const visited: [number, number][] = [[0, 0]];

function contains(arr: [number, number][], i: number, j: number): boolean {
  return arr.findIndex((x) => x[0] === i && x[1] === j) !== -1;
}

function move_tail(h: [number, number], t: [number, number]): [number, number] {
  console.log("head", h);
  if (Math.abs(h[0] - t[0]) <= 1 && Math.abs(h[1] - t[1]) <= 1) {
    return [t[0], t[1]];
  }
  if (h[0] == t[0] && h[1] - t[1] > 1) {
    return [t[0], t[1] + 1];
  }
  if (h[0] == t[0] && h[1] - t[1] < -1) {
    return [t[0], t[1] - 1];
  }
  if (h[1] == t[1] && h[0] - t[0] > 1) {
    return [t[0] + 1, t[1]];
  }
  if (h[1] == t[1] && h[0] - t[0] < -1) {
    return [t[0] - 1, t[1]];
  }
  if (h[0] == t[0] - 2) {
    return [t[0] - 1, h[1]];
  }
  if (h[0] == t[0] + 2) {
    return [t[0] + 1, h[1]];
  }
  if (h[1] == t[1] - 2) {
    return [h[0], t[1] - 1];
  }
  if (h[1] == t[1] + 2) {
    return [h[0], t[1] + 1];
  }

  return [-1, -1];
}

let head: [number, number] = [0, 0];
let tail: [number, number] = [0, 0];

for (const move of moves) {
  const t = move.split(" ");
  const direction = t[0];
  const steps = parseInt(t[1]);

  for (let i = 0; i < steps; i++) {
    switch (direction) {
      case "R":
        head = [head[0] + 1, head[1]];
        break;
      case "L":
        head = [head[0] - 1, head[1]];
        break;
      case "U":
        head = [head[0], head[1] + 1];
        break;
      case "D":
        head = [head[0], head[1] - 1];
        break;
    }
    tail = move_tail(head, tail);
    if (!contains(visited, tail[0], tail[1])) {
      visited.push(tail);
    }
  }
}

console.log("Positions visited", visited.length);
