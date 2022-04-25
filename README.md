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
### EPIC 6: Wishlist
## Site owner goals
## Structure
## Design Choises
### Fonts
### Colors
Colours for the website is inpired by the Northen Lights magical colours.
![nothen light](https://github.com/StinaAxelsson/project-5/blob/main/media/norrsken.jpg)
### Colour Schema
![color scheme](https://github.com/StinaAxelsson/project-5/blob/main/media/colorscheme.jpg)
## Wireframes
  * [Desktop]()
  * [Tablet]()
  * [Mobile]()

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
  * AWS
  * Heroku
  * Git
  * Postgres
## Other programmes
  * [AWS storage]()- Store all the static files
  * [Stripe]()- Make secure payments
  * [Heroku]()- Deploy my site
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

# Testing
## Manually testing by user stories
## Validator testing
## Bugs

# Deployment
# Credits

Descriptions of the products: https://www.gemstone.org/

https://thecrystalcouncil.com/

https://www.adlibris.com/

https://sagecrystals.com/
# Acknowledgements

