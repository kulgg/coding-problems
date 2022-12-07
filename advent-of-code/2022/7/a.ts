const text = await Deno.readTextFile("input.txt");

const dirs: { [id: string]: number } = {};
const max_size = 100000;
const current_dir: string[] = [];

const lines = text.split("\n");

for (const line of lines) {
  if (line.startsWith("$ ls") || line.startsWith("dir")) {
    continue;
  }
  if (line.startsWith("$ cd ..")) {
    if (current_dir.length > 1) {
      current_dir.pop();
    }
  } else if (line.startsWith("$ cd")) {
    current_dir.push(line.slice(5));
  } else {
    const fileSize = parseInt(line.split(" ")[0]);
    console.log(line);
    current_dir.forEach((dir) => {
      if (!dirs[dir]) {
        dirs[dir] = 0;
      }
      dirs[dir] += fileSize;
    });
  }
}

const dirNames = Object.keys(dirs);
// console.log("dirs", dirs);

console.log("\n");

console.log(
  dirNames
    .filter((name) => dirs[name] <= max_size)
    .reduce((sum, name) => {
      return sum + dirs[name];
    }, 0)
);
