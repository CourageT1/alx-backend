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

// Function to set a new school in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Function to display the value of a school
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
};

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
