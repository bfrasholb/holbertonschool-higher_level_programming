#!/usr/bin/node

args = process.argv.slice(2);
if (args[0]) console.log(args[0]);
else if (args[0] === undefined) console.log('No argument');
