![Responsive image here]()

# Project Description
This project is developed as my 5th and final portfolio project during my course at Code Institute. It is a e-commerce website. Here you can find all you need in the world of crystals and gemstones. You can register an account for save your information and order history, you can save your favourite products to a personal wishlist, read and write reviews on the products you like or dislike. And of course buy your magical stuff secure and safe with stripe pay system! 

Here is a livelink to the project: [Crystalizedshop](https://crystalizedshop.herokuapp.com/)

**Cardnumber:** 4242 4242 4242 4242   
**Date:**24/02
**CVC:** 424   
**Postnumber:** 42424   

# Content
* [Project Description](https://github.com/StinaAxelsson/crystalize-pp5#project-description)
* [UX](https://github.com/StinaAxelsson/crystalize-pp5#ux)
  * [User Stories](https://github.com/StinaAxelsson/crystalize-pp5#user-stories)
  * [Site Owner Goals](https://github.com/StinaAxelsson/crystalize-pp5#site-owner-goals)
  * [Structure](https://github.com/StinaAxelsson/crystalize-pp5#structure)
  * [Design Choises](https://github.com/StinaAxelsson/crystalize-pp5#design-choises)
  * [Wireframes](https://github.com/StinaAxelsson/crystalize-pp5#wireframes)
* [Features](https://github.com/StinaAxelsson/crystalize-pp5#features)
  * [Data Storage](https://github.com/StinaAxelsson/crystalize-pp5#data-storage)
  * [Existing Features](https://github.com/StinaAxelsson/crystalize-pp5#existing-features)
  * [Features Left to Implement](https://github.com/StinaAxelsson/crystalize-pp5#features-left-to-implement)
  
* [Technologies Used](https://github.com/StinaAxelsson/crystalize-pp5#technologies-used)
  * [Languages](https://github.com/StinaAxelsson/crystalize-pp5#languages)
  * [Frameworks](https://github.com/StinaAxelsson/crystalize-pp5#frameworks)
  * [Other Programmes](https://github.com/StinaAxelsson/crystalize-pp5#other-programmes)
  
* [Testing](https://github.com/StinaAxelsson/crystalize-pp5#testing)
  * [Manually test user storys](https://github.com/StinaAxelsson/crystalize-pp5#manually-testing-by-user-stories)
  * [Validator test](https://github.com/StinaAxelsson/crystalize-pp5#validator-testing)
  * [Bugs](https://github.com/StinaAxelsson/crystalize-pp5#bugs)
  
* [Deployment](https://github.com/StinaAxelsson/crystalize-pp5#deployment)
* [Credits](https://github.com/StinaAxelsson/crystalize-pp5#credits)
* [Acknowledgements](https://github.com/StinaAxelsson/crystalize-pp5#acknowledgements)

# UX 
## User stories
### EPIC 1: Navigation
* As a user I can view all the products in store so that **I can easy scroll and choose what to buy**
* As a user I can navigate the site from wherever I am on the site so that I can have a good user experience
* As a user I can **get a visual feedback** so that I can see that an action has been completed
* As a user I can search for a product so that I find the item that I was looking for
### EPIC 2: Shopper
* As a shopper I can easy see my cart total so that I have a overview of my shopping budget
* As a shopper I can sort the list of available products by name or price or alphabetic order so that I easily can sort and get an overview of the products that I am looking for

### EPIC 3: Profile
* As a user I can create an account and register a profile so that **I can view my order history and confirmations, and save my payment information**
* As a user I can easy login or logout from my account so that I can access my profile information
* As a user I can add products, update the quantity, or delete products in my cart so that easily make changes before I pay

### EPIC 4: Checkout
* As a shopper I can view a total grand price of my order before completing my purchase so that I can see what the price will be and no mistakes have been done
* As a shopper I can **know that my payment and personal information are totally secure.** so that I can go through the purchase safe and secure.
* As a shopper I can receive a confirmation email of my purchase so that I know my purchase went through successfully.

### EPIC 5: Reviews
* As a user I can read other users reviews on products so that Im able to get knowledge of others opinions of the product
* As a user I can add an review of the products so that I can share my opinion about it to other potential buyers

### EPIC 6: Wishlist
* As a shopper I can Choose to add a item to a wishlist page so that I can save my favourites product but not yet decide if I want to buy it
* As a user I can delete a item from my wishlist if I don't want it anymore so that I can control my wishlist page and clean it from unwanted items
* As a user I can Easy navigate to the item in my saved wishlist so that I can choose to put it in the cart if I wanted to buy it
## Site owner goals
## Structure
## Design Choises
### Fonts
I have used the font 'Julius Sans One' for all the Rubrics on the site, it is a clean and soft font that match the theme. And for the rest of the texts I am using 'Roboto' just because it is nice to read and don't take any attention.
### Colors
THe colors for this site is white and different shades of purple. It is a soft and calm colour that match the theme and the product of the site. Indicate a calm feeling for the user. 
### Colour Schema
![color scheme](https://github.com/StinaAxelsson/project-5/blob/main/media/colorscheme.jpg)
## Wireframes
  * [Browser](https://github.com/StinaAxelsson/crystalize-pp5/blob/main/media/images/wireframe-browser.pdf)
  * [Tablet](https://github.com/StinaAxelsson/crystalize-pp5/blob/main/media/images/wireframe-tablet.pdf)
  * [Mobile](https://github.com/StinaAxelsson/crystalize-pp5/blob/main/media/images/wireframe-mobile.pdf)

## Existing features

**Navigation**
* Navigation bar on top of the site. When used on smaller devices manu is in a dropmenu.
**Home**
* Hero Image
* Grid with linked images of all categories
**Products**
**List of all products**
**Sort all products by:**
  * Price(low to high) and vice verse
  * Rating(low to high) and vice verse
  * Name (A-Z) and vice verse
  * Category (A-Z) and vice verse
**Product detail page with all detail information of the specific product**
  * product name, price and review count.
  * Add to cart button
  * Description of the product
**Add products to shopping cart**
  * Success message and overview of whats in the cart and the total cost.
  * Add more quantity in bag or remove products from bag
**Checkout**
  * Create secure purchases
  * Create a user profile to store userse order information 
  * Receive confirmation email of the purchase with order number and information
**Profile**
  * Register a profile account to store information and save all order history
  * Update users informaion on profile 
  * Sign in / Register and Sign out
  * E-mail verification when register an account
**Review**
  * Users can read other users reviews of the product and see a avarage rating if its rated
  * Logged in user can add reviews on products
**Wishlist**
  * As a logged in user you can save your favourit product items in a own wishlist page
  * Delete wishlist items from the list
  * See what product is marked as wish in product list


## Features left to implement
* Add product to shopping cart direct from the product list instead of only from the product detail page.
* Add to wishlist direct from product list instead of only from the product detail page.
* Allow user to edit their posted reviews
## Data Storage
### Review model
| Title       	| Key in Database   	| Form Validaton    	| Data Type     	|
|-------------	|-------------------	|-------------------	|---------------	|
| User        	| User, primary_key 	| None              	| ForeignKey    	|
| Product     	| product           	| None              	| ForeignKey    	|
| Title       	| title             	| max_length=50     	| CharField     	|
| Review body 	| review_body       	| max_length=250    	| TextField     	|
| Rating      	| rating            	| choices=RATE      	| IntegerField  	|
| Date 	| date_posted       	| auto_now_add=True 	| DateTimeField 	|

### Wishlist Model
| Title       	| Key in Database   	| Form Validaton 	| Data Type  	|
|-------------	|-------------------	|----------------	|------------	|
| Product     	| product           	| None           	| ForeignKey 	|
| User profile 	| logged_user	| None           	| ForeignKey 	|

### Profile Model
| Title                     	| Key in Database           	| Form Validaton 	| Data Type     	|
|---------------------------	|---------------------------	|----------------	|---------------	|
| User                      	| User, primary_key         	| None           	| OneToOneField 	|
| Phone number      	| default_phone_number      	| max_length=20  	| CharField     	|
| Country           	| default_country           	| Country*       	| CountryField  	|
| Postcode          	| default_postcode          	| max_length=20  	| CharField     	|
| Town or city      	| default_town_or_city      	| max_length=40  	| CharField     	|
| Delivery Address 1 	| default_delivery_address1 	| max_length=80  	| CharField     	|
| Delivery Address 2 	| default_delivery_address2 	| max_length=80  	| CharField     	|
| Country           	| default_country           	| max_length=80  	| CharField     	|

### Products Model
| Title       	| Key in Database 	| Form Validaton 	| Data Type    	|
|-------------	|-----------------	|----------------	|--------------	|
| Category    	| category        	| None           	| ForeignKey   	|
| Sku         	| sku             	| max_length=254 	| CharField    	|
| Name        	| name            	| max_length=254 	| CharField    	|
| Description 	| description     	| None           	| TextField    	|
| Price       	| price           	| max_digits=6   	| DecimalField 	|
| Image       	| image           	| None           	| ImageField   	|
| Rating      	| rating          	| max_digits=6   	| DecimalField 	|


# Technologies used
## Languages
  * HTML5
  * CSS3
  * Javascript
  * Python
## Frameworks
  * Django
  * Bootstrap
## Libraries
  * Jquery
  * Stripe Payments
## Tools
  * * [AWS storage]()- Store all the static files
  * [Heroku]()- Deploy my site
  * Git
  * Postgres
## Other programmes
  * [Stripe]()- Make secure payments
  * [Gitpod]()- Development workspace
  * [Github]()- Store my repository, code and user stoys
  * [Balsamiq]()- Make my wireframes 
  * [Google Fonts]()- Got my fonts
  * [W3C Validator]()- Valitade CSS and HTML code
  * [JShint]()- Validate javascript code
  * [Pep8]()- Validate python code
  * [Color palett generator]()- generate a plaett with color hexadecimals
  * [Chrome Devtools]()- Helpful during development to find bugs, and issues
  * [Markdown table generator]()- Generate table for readme
  * [Pixlr](https://pixlr.com/se/x/#home)- Create the logo image

# Testing
## Manually testing by user stories
### EPIC 1: Navigation
**Implementations:** As a user I can view all the products in store so that I can easy scroll and choose what to buy  
**Test:** Tested this by view the homepage and try to navigate from the navigation bar to products, where all products is find and it is easy to scroll.   
**Result:** This test pass and works  

**Implementations:** As a user I can navigate the site from wherever I am on the site so that I can have a good user experience  
**Test:** Tested this and all products is well sorted throughout the website in the navigationbar and can be reach from all different screen sizes.  
**Result:** This test pass and works

**Implementations:** As a user I can get a visual feedback so that I can see that an action has been completed.  
**Test:** I tested this by add products to cart, add to wishlist, sign in, make a purshase and update or delete an item from shoppingcart and I get an informational feedback message in all of the above actions.  
**Result:** This test passed and works.

**Implementations:**  As a user I can search for a product so that I find the item that I was looking for  
**Test:** In the main navigation bar, there is a search icon where you can search by name, category, words from the product description and get the results by the search query. Or get a message that my search didn't work.  
**Result:** This test passed and works.  
### EPIC 2: Shopper
**Implementations:** As a shopper I can easy see my cart total so that I have a overview of my shopping budget  
**Test:** In the right corner of the website, there is a cart-icon with the cart total of what I as a shopper has added and can be seen from all the pages and different screen devices.  
**Result:**  This test pass and works  

**Implementations:** As a shopper I can sort the list of available products by name or price or alphabetic order so that I easily can sort and get an overview of the products that I am looking for    
**Test:** I tested this by click on the sort dropdown in products page, as a user i can chose to sort my product view by name(A-Z)/(Z-A), By rating high to low/low to high, category(A-Z)/(Z-A) and price low to high/ high to low  
**Result:**  This test pass and works in all ways.  
### EPIC 3: Profile
**Implementations:** As a user I can create an account and register a profile so that I can view my order history and confirmations, and save my payment information  
**Test:**  I tested this by register an account and make a purshase. In my profile page I got my profile information stored and can be updated. My order history is saved.  
**Result:** This test pass

**Implementations:** As a user I can easy login or logout from my account so that I can access my profile information  
**Test:** Tested this by click on my profile in the navigationbar and can choose to logout. Or if I am logged out I can sign in from the same place.  
**Result:** This test pass  

**Implementations:** As a user I can add products, update the quantity, or delete products in my cart so that easily make changes before I pay  
**Test:** In the shoppingcart I got all the products that I have added, I can easy update or remove products from the cart and get a nice overview before checkout.  
**Resul:t** This test pass

### EPIC 4: Checkout
**Implementations:**  As a shopper I can view a total grand price of my order before completing my purchase so that I can see what the price will be and no mistakes have been done  
**Test:**  In shoppingcart there is an grand total with added delivery cost if purshase is smaller than $50, easy to see before checkout  
**Result:**  This test pass  

**Implementations:** As a shopper I can know that my payment and personal information are totally secure. so that I can go through the purchase safe and secure.   
**Test:**  Using stripe with webhooks, and secure checkout there is safe to go through the payment and purshase.
**Result:**  This test pass

**Implementations:**  As a shopper I can receive a confirmation email of my purchase so that I know my purchase went through successfully.  
**Test:** When payment is successful the user get an confirmation mail with the orderinformation and ordernumber. The purshase is saved on users profile page in order history. And you get an instant confirmation when payment is done.  
**Result:**  This test pass

### EPIC 5: Reviews
**Implementations:** As a user I can read other users reviews on products so that Im able to get knowledge of others opinions of the product  
**Test:**  On products where there is reviews, its easy to find them and read from the product detail page.  
**Result:**  This test pass  

**Implementations:**  As a user I can add an review of the products so that I can share my opinion about it to other potential buyers  
**Test:** Tested this by click on a product detail page when not logged in and get informed that I have to sign in so that I can then make reviews from the product detail page with no problem.  
**Result:**  This test pass  

### EPIC 6: Wishlist
**Implementations:**  As a shopper I can Choose to add a item to a wishlist page so that I can save my favourites product but not yet decide if I want to buy it  
**Test:**  I tested this as not loged in and redirect to sign in. When a user is logged in you can save products to your personal wishlist that you only can see if you are a logged in user.  
**Result:**  This test pass.  

**Implementations:**  As a user I can delete a item from my wishlist if I don't want it anymore so that I can control my wishlist page and clean it from unwanted items  
**Test:**  Tested this by click on my wishlist page and from there I can delete items from my list.    
**Result:** This test pass.  

**Implementations:**  As a user I can Easy navigate to the item in my saved wishlist so that I can choose to put it in the cart if I wanted to buy it   
**Test:** Tested this by click on my wishlist page and from there link back to the product detail page for add it to my cart if I want.   
**Result:**  This test pass.  

## Validator testing
## Bugs

# Deployment
# Credits

Descriptions of the products: https://www.gemstone.org/

https://thecrystalcouncil.com/

https://www.adlibris.com/

https://sagecrystals.com/
# Acknowledgements

