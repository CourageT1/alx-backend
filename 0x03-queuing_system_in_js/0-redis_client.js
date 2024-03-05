import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Connect to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors
client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err);
});

// Close the Redis connection when the script is terminated
process.on('SIGINT', () => {
  client.quit();
  process.exit();
});
