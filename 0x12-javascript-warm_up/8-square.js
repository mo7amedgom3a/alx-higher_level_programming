#!/usr/bin/node
const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    let line = '';
    for (let j = 0; j < num; j++) {
      line += '#';
    }
    console.log(line);
  }
}
