#!/usr/bin/node

const args = process.argv.slice(2);
const myNumber = parseInt(args[0], 10);
if (myNumber) console.log('My number:', myNumber);
else console.log('Not a number');
