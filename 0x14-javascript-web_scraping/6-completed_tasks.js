#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });
    console.log(completedTasksByUser);
  }
});
