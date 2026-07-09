#!/usr/bin/node

const args = process.argv.slice(2);
my_number = parseInt(args[0], 10)
if (my_number) console.log('My number:', my_number)
else console.log('Not a number')
