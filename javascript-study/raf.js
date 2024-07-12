console.time("raf");

console.log(
  "Memory usage before const:",
  process.memoryUsage().heapUsed / 1024 / 1024,
  "MB",
);

// const rawSequences = Array.from({ length: 10000000 }, (_, i) => {
//   return i.toString().padStart(7, "0");
// });

const rawSequences = Array.from({ length: 100000000 }, (_, i) => {
  return i;
});
// //
// const rawSequences = Array.from({ length: 100000000 }, (_, i) => {
//   const hexValue = i
//   return Number(hexValue);
// });

for (let i = rawSequences.length - 1; i > 0; i--) {
  const j = Math.floor(Math.random() * (i + 1));
  [rawSequences[i], rawSequences[j]] = [rawSequences[j], rawSequences[i]];
}

console.log(
  "Memory usage after const:",
  process.memoryUsage().heapUsed / 1024 / 1024,
  "MB",
);

console.log(
  "Memory usage of array:",
  (rawSequences.length * 100) / 1024 / 1024,
  "MB",
);

console.timeEnd("raf");
