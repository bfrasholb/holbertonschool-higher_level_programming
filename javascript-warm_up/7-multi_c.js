#!/usr/bin/node

const arg = process.argv[2];
let occurences = parseInt(arg, 10);
if (occurences) {
  while (occurences > 0) {
    console.log('C is fun');
    occurences = occurences - 1;
  }
} else {
  console.log('Missing number of occurences');
}
