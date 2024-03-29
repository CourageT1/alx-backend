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

// Function to create hash values using hset
const createHash = () => {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
};

// Function to display the hash using hgetall
const displayHash = () => {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
};

// Call the functions
createHash();
displayHash();
