#!/usr/bin/node

function add (...args) {
  let result = 0;
  if (args.length > 0) {
    let i = 0;
    while (i < args.length) {
      result += args[i];
      i += 1;
    }
  }
  return result;
}

module.exports = {
  add
};
