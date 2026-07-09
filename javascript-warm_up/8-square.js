#!/usr/bin/node

let i = 0;
let j = 0;
let row = ''
const size = process.argv.slice(2);

if (size === undefined) {
    console.log('Missing size');
    return 0;
}
while (i < size) {
    while (j < size) {
        row += 'X'
        j += 1;
    }
    console.log(row)
    i += 1
}
