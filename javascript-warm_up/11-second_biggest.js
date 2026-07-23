#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

function second_best(args) {
    let result = 0;
    if (args.length === 0 || args.length === 1) {
        return result;
    } else {
        return args.sort((a, b) => b - a)[1];
    }
}

console.log(second_best(args));
