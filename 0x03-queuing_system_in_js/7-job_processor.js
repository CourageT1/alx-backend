import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send a notification
const sendNotification = (phoneNumber, message, job, done) => {
  // Track progress
  job.progress(0, 100);

  // If phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress
  job.progress(50, 100);

  // Log sending notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
};

// Create a Kue queue for processing jobs
const queue = kue.createQueue({ concurrency: 2 }); // Process two jobs at a time

// Process jobs in the push_notification_code_2 queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract phone number and message from job data
  const { phoneNumber, message } = job.data;

  // Call sendNotification function with phone number, message, job, and done callback
  sendNotification(phoneNumber, message, job, done);
});
