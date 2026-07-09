#!/usr/bin/node

const args = process.argv.slice(2);
if (args[0]) if (parseInt(args[0], 10)) console.log('My number: ', args[0])
else console.log('Not a number')
