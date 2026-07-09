#!/usr/bin/node

const secrets = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let line = 0;
while (secrets[line]) {
  console.log(secrets[line]);
  line = line + 1;
}
