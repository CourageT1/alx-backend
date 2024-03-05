import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

// Import createPushNotificationsJobs function

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a queue with Kue
    queue = kue.createQueue();
    // Enter test mode without processing the jobs
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit the test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    // Call createPushNotificationsJobs with a non-array argument
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    // Expect no jobs to be created in the queue
    expect(queue.testMode.jobs.length).to.equal(0);
  });

  it('should create two new jobs to the queue', () => {
    // Define array of jobs
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    // Call createPushNotificationsJobs with the array of jobs
    createPushNotificationsJobs(jobs, queue);

    // Expect two jobs to be created in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Validate job data
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
    expect(queue.testMode.jobs[0].data.message).to.equal('This is the code 1234 to verify your account');

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('4153518781');
    expect(queue.testMode.jobs[1].data.message).to.equal('This is the code 5678 to verify your account');
  });
});
