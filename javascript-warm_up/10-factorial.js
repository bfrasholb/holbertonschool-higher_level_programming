#!/usr/bin/node

const args = parseInt(process.argv.slice(2)[0]);

function factorial (args) {
  if (isNaN(args) || args === 1) {
    return 1;
  } else {
    return args * factorial(args - 1);
  }
}

console.log(factorial(args));
