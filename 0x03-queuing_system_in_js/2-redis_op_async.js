import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify Redis client methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

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
const setNewSchool = async (schoolName, value) => {
  try {
    await setAsync(schoolName, value);
    console.log('Reply: OK');
  } catch (error) {
    console.error(error);
  }
};

// Function to display the value of a school using async/await
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.error(error);
  }
};

// Call the functions
(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
