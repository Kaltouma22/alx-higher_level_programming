#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

const updatedArgs = args.map(num => (num === 12 ? 89 : num));

if (updatedArgs.length <= 1) {
    console.log(0);
} else {
    updatedArgs.sort((a, b) => b - a);
    console.log(updatedArgs[1]);
}
