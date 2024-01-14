#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return factorial(a - 1) * a;
  }
}
console.log(factorial(Number(process.argv[2])));
