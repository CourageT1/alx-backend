import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Function to send a notification
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs in the push_notification_code queue
queue.process('push_notification_code', (job, done) => {
  // Extract phone number and message from job data
  const { phoneNumber, message } = job.data;

  // Call sendNotification function with phone number and message
  sendNotification(phoneNumber, message);

  // Call done when job processing is complete
  done();
});
