#!/usr/bin/node
const fs = require('fs').promises;

async function concatFiles () {
  try {
    const fileA = await fs.readFile(process.argv[2], 'utf8');
    const fileB = await fs.readFile(process.argv[3], 'utf8');
    const concatenatedfile = fileA + fileB;
    await fs.writeFile(process.argv[4], concatenatedfile);
  } catch {
    // Nothing
  }
}

concatFiles();
