import redis from 'redis';

// Create a Redis client for publishing
const publisher = redis.createClient();

// Connect to the Redis server
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors
publisher.on('error', (err) => {
  console.error('Redis client not connected to the server:', err);
});

// Function to publish message after a specified time
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school', message);
  }, time);
};

// Call the publishMessage function with different messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
