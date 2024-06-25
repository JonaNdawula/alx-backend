const express = require('express');
const { promisify } = require('util');
const redis = require('redis');


const listProducts = [
  {itemId:1, itemName: "Suitcase 250", price :50,  initialAvailableQuantity:  4},
  {itemId:2, itemName: "Suitcase 450", price :100, initialAvailableQuantity: 10},
  {itemId:3, itemName: "Suitcase 650", price :350, initialAvailableQuantity:  2},
  {itemId:4, itemName: "Suitcase 1050",price :550, initialAvailableQuantity:  5}]


function getItemById(id) {
  return listProducts.filter((product) => product.itemId === id)[0];
}

const user = redis.createClient();
const getAsync = promisify(user.get).bind(user);

user.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

user.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  user.set(`item.${itemId}`, stock);
} 

async function getCurrentReservedStockById(itemId) {
  const prodStock = await getAsync(`item.${itemId}`);
  return prodStock;
}

const app = express();

app.listen(1245, () => {
  console.log('app listening at http://localhost:1245');
});

app.get('/list_products', (req, resp) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const id = Number(req.params.itemId);
  const prod = getItemById(id);

  if (!prod) {
    res.json({status : 'Product not found'});
    return;
  }

  const availableStock = await getCurrentReservedStockById(id);
  if (!availableStock) {
    await reserveStockById(id, prod.stock);
    prod.availableQuantity = prod.stock;
  } else prod.availableQuantity = availableStock;
  res.json(prod);
});

app.get('/reserve_product/:itemId', async (req, res) => {
   const id = Number(req.params.itemId);
   const prod = getItemById(id);
   
   if(!prod) {
     res.json({ status: 'Product not found'});
     return;
   }
   
   let availableStock = await getCurrentReservedStockById(id);
   if (availableStock === null) availableStock = prod.stock;

   if ( availableStock <= 0) {
     res.json({status: 'Not enough stock available', id});
     return;
   }

   reserveStockById(id, Number(availableStock) - 1);

   res.json({ status: 'Reservation confirmed', id });
 
});
