#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
console.log(Number.isNaN(num) ? 'Not a number' : `My number: ${num}`);
