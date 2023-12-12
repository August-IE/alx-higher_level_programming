#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

const addToNewDict = (value, key) => {
  if (!newDict[value]) {
    newDict[value] = [key];
  } else {
    newDict[value].push(key);
  }
};

for (const key in dict) {
  const value = dict[key];
  addToNewDict(value, key);
}

console.log(newDict);
