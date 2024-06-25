import chai from 'chai';
import kue  from 'kue';
import createPushNotificationsJobs from './8-job';

const expect = chai.expect;

describe('createPushNotificationsJobs', function() {
  let queue;
  
  before(function() {
    
   queue = kue.createQueue();

   if (kue.testMode) {
     kue.testMode.enter();
   }
  });

  after(function() {
    if (kue.testMode && kue.testMode.exit) {
    kue.testMode.exit();
    }
  });


  beforeEach(function() {
    if (kue.testMode && kue.testMode.clear) {
    kue.testMode.clear();
    }
  });
 
  it('should throw an error if jobs is not an arry', function (){
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });
  
  it('should create a job for each items in the jobs array', async function(){
    const jobs = [
      { phoneNumber: '1234567890', message: 'Message 1' },
      { phoneNumber: '0987654321', message: 'Message 2' }
    ];
	  
    await createPushNotificationsJobs(jobs,queue);
     
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);


  });


});
