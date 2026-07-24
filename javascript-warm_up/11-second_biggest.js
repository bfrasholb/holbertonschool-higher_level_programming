#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

function SecondBest (args) {
  const result = 0;
  if (args.length === 0 || args.length === 1) {
    return result;
  } else {
    return args.sort((a, b) => b - a)[1];
  }
}

console.log(SecondBest(args));
