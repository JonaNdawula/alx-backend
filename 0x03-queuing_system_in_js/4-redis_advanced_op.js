import redis from 'redis';
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err)=>{
  console.error(`Redis client not connect to the server: ${err.message}`);
});

const schools = {
  'Portland': '50',
  'Seattle': '80',
  'New York': '20',
  'Bogota': '20',
  'Cali': '40',
  'Paris': '2'
};

Object.entries(schools).forEach(([city, value]) => {
  client.hset('HolbertonSchools', city, value, redis.print);
});

client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(obj);
});
