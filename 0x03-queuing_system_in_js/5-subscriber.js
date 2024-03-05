import redis from 'redis';

// Create a Redis client for subscribing
const subscriber = redis.createClient();

// Connect to the Redis server
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors
subscriber.on('error', (err) => {
  console.error('Redis client not connected to the server:', err);
});

// Subscribe to the channel 'holberton school'
subscriber.subscribe('holberton school');

// Listen for messages on the subscribed channel
subscriber.on('message', (channel, message) => {
  console.log(message);

  // If message is 'KILL_SERVER', unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
