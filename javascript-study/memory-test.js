// import { randomUUID } from 'node:crypto';

const { randomUUID } = require('crypto');

console.log('Memory usage before const:', process.memoryUsage().heapUsed / 1024 / 1024, 'MB');

const myTenMillionElementArray = new Array(10000000).map((_, i) => ({
  id: i,
  name: `Element ${i}`,
  anotherThing: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
  uuid: randomUUID(),
}));

console.log('Memory usage after const:', process.memoryUsage().heapUsed / 1024 / 1024, 'MB');

console.log('Memory usage of array:', (myTenMillionElementArray.length * 100) / 1024 / 1024, 'MB');
