#!/usr/bin/node

let i = 0;
let j = 0;
let row = ''
const size = parseInt(process.argv.slice(2), 10);

if (size) {
    while (i < size) {
        while (j < size) {
            row += 'X'
            j += 1;
        }
        console.log(row)
        i += 1
    }
    return 0;
}

console.log('Missing size')
