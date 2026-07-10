#!/usr/bin/node

const args = process.argv.slice(2);
function add (a, b) {
  console.log(parseInt(a, 10) + parseInt(b, 10));
}
add(args[0], args[1]);
