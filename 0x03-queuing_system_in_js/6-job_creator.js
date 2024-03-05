import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Notification message',
};

// Create a job in the push_notification_code queue
const job = queue.create('push_notification_code', jobData);

// When the job is created without error
job.on('created', () => {
  console.log(`Notification job created: ${job.id}`);
});

// When the job is completed
job.on('complete', () => {
  console.log('Notification job completed');
});

// When the job fails
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
