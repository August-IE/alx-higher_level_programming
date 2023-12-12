#!/usr/bin/node
exports.logMe = (() => {
  let count = 0;
  return function (item) {
    console.log(`${count++}: ${item}`);
  };
})();
