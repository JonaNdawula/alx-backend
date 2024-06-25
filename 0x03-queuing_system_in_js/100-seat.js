const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');


const app = express();
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
const queue = kue.createQueue();

let reservationEnabled = true;

client.on('error', (error) => console.log('Redis Client Error', error));

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
}

async function initializeSeats() {
  await reserveSeat(50);
}

initializeSeats();



app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json( {numberOfAvailableSeats: seats});
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({status: 'Reservation are blocked'});
  }
  const job = queue.create('reserve_seat', {})
    .save((error) => {
      if (error) {
        return res.json({ status: 'Reservation failed'});
      }
      res.json({ status: 'Reservation in process'});
    })
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    let seats = await getCurrentAvailableSeats(); 
    if (seats > 0) {
      await reserveSeat(--seats);
      if ( seats === 0) {
        reservationEnabled = false;
      }
      done();
    } else {
      done(new new Error('Not enough seats available '));
    }
  });
  res.json({status: 'Queue processing'});
});

queue.on( 'job complete', (id, result) => {
   console.log(`Seat reservation job ${id} completed`);
}).on('job failed', (id, error) => {
  kue.job.get(id, (err, job) => {
    if (err) return;
  console.log(`Seat reservation job ${id} failed: ${error}`);
  });
});

app.listen(1245, () => console.log('server listening on port 1245'));
