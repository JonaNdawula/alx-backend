import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test message',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) =>{
    if (err) {
      console.error('Failed to create job', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (errormessage) => {
  console.log('Notification job failed', errorMessage);
});
