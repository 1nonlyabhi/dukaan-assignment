<h1 align='center'>
  Hi there 👋 I'm Abhishek 👨‍💻
</h1>

<p align='center'>
  This is the Assessment Task submitted by me for Backend Developer Role.
</p>



<p align='center'>

  <a href="https://www.linkedin.com/in/1nonlyabhi/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>&nbsp;&nbsp;
  <a href="https://twitter.com/1nonlyabhi">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" />        
  </a>&nbsp;&nbsp;

</p>


## Setup

1. Git Clone the project with: ```git clone https://github.com/1nonlyabhi/dukaan-assignment```.

2. Move to the base directory: ```cd dukaan-assignment```

3. Create a new python enveronment with: ```python -m venv dukaan-env```.

4. Activate enveronment with: ```dukaan-env\Scripts\activate``` on windows, or ```source dukaan-env/bin/activate``` on Mac and Linux.

5. Install required dependences with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

7. Run app localy with: ```python manage.py runserver```.

8. Download postman from: ```https://www.postman.com/downloads/```.


## Task: 
Dukaan is a tech platform that enables a business to quickly set up and run an online retail store.

A typical seller installs the Dukaan app, Signs up using his mobile number and creates his store. He can then start uploading inventory (as products) to his store.
Once the store is created, he can share the store link with his/her customers on social media and starts accepting online orders.  
 
Your assignment is to Design a very basic API (Django DRF) & database (any SQL db works) structure which supports above work-flow.

### Detailed breakdown of the workflow -

 ### endpoints for seller side. (Words in Bold indicates table names)

 
1.  seller signs up using his mobile number that creates an **account**
    1.  Take mobile number & OTP (random) as input to the API
    2.  Create customer account in accounts table.
    3.  Issue a token.
   

2.  seller creates his **store**
    1.  Take store name & address as input.  
    2.  Create store in store table. One seller can have multiple stores.
    3.  Generate a unique store link based on his store name.
    4.  Respond back with storeid and link.

3.  seller starts uploading inventory in the form of **products** and **categories**. 
    1.  Take product name, description, MRP, Sale price, image & category as input.  
    2.  Create a category if it doesn't exist.
    3.  Create product
    4.  Respond back with id, name and image.

 
4.  Seller can accept **orders** from his **customers**. 
    1.  Create a customer table with a mobile number as unique and address details.    
    2.  Create a order table to store orders data.
    3.  When someone places an order from the buyer side, the records will be saved here.
 

### Endpoints for Buyer side

 
1.  Seller shares his store link with his customers. To get basic store details 
    1.  Take store link as input    
    2.  Respond back with storeId, store name, address

2.  To get product catalog & categories 
    1.  Take storelink as input    
    2.  Respond back with the catelog, grouped by categories & sorted by number of products in the category.


3.  people (Un-authenticated users) can add items into their cart.
    1.  Maintain a cart on the server (create appropriate models for this)
    2.  On cart change (add / remove item) update the cart on server
    3.  For cart line items take product id, qty, storeLink as input and fetch product meta data from the DB and save them.
 

4.  Customer place an order for a product.
    1.  Identity customer using JWT or token which can be generated using his mobile number and a OTP
    2. Bypass the actual OTP validation flow and issue a token on any random number & OTP combination
    3.  Create a customer record if didn’t already exist for that mobile number.
    4.  Take the cart object as input and convert that into an order.
    5.  Create an order for that store & customer and return back the order id.



## Requests

##### _Requests including * needs Authorization Token in Headers_
##### _Few of the endpoints support PUT, DELETE request too_

#### Register the user & getting token

`POST localhost:8000/api/account/signup`

    {
        "mobile_num": "+911234567890",
        "password": "password"
    }

#### For only getting token

`POST localhost:8000/api/account/login`

    {
        "username": "username",
        "password": "password"
    }


#### To create store & getting link*

`POST localhost:8000/api/store/`

    {
        "store_name": "New Shop 3",
        "address": "Gorakhpur, Uttar Pradesh, India"
    }


#### Getting all store data of a seller*

`GET localhost:8000/api/store/`


#### To fetch a store's detail and its product

`GET localhost:8000/api/store/<store-slug>`


#### To add product in a store*

`POST localhost:8000/api/store/2rsh2n-new-shop/product`

    {
        product details (like: product_name, image etc) through form data
    }
    

#### To the catelog, grouped by categories & sorted by number of products in the category

`GET localhost:8000/api/store/2rsh2n-new-shop/category`
* _Tried to implement it but Not working and facing some issue_


* _Tried implementing rest of the endpoints but didn't get much time but learnt so much, I'll try to solve them too._

