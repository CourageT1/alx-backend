import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const client = redis.createClient();

// Promisify Redis functions
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// Create Kue queue
const queue = kue.createQueue();

// Reserve initial 50 seats
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Get the current number of available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats);
}

// Initialize available seats to 50
reserveSeat(50);

// Initialize reservation enabled flag
let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  // Create and queue a job
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      console.error(err);
      return res.json({ status: 'Reservation failed' });
    }
    console.log(`Seat reservation job ${job.id} completed`);
    return res.json({ status: 'Reservation in process' });
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the queue
  queue.process('reserve_seat', async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    availableSeats -= 1;

    if (availableSeats === 0) {
      reservationEnabled = false;
    }

    if (availableSeats >= 0) {
      await setAsync('available_seats', availableSeats);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

// Start the server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
