# loopitoy


loopitoy is an Austrian eCommerce platform to buy second-hand toys. The platform aims at supporting a circle economy for toys as it also offers to sell toys that are not used anymore. This website is the final project at Code Institute. The website is built mainly in Python, using the Django framework.  

The deployed website can be viewed [here](https://loopitoy-2943fdc3b2bc.herokuapp.com/).

![Mockup](./docs/mockup.PNG)


# Content
- [UX Design](#ux)
    - [Strategy: User Stories](#strategy)
    - [Structure: ERD Model](#structure)
    - [Skeleton: Wireframes](#skeleton)
    - [Surface: Fonts & Colors & Images](#surface)
- [Features](#Features)
- [Business Model: SEO & Marketing](#business-model)
- [Testing & Validation](#testing--validation)
- [Technologies Used](#technologies-used)
- [Deployment & Forking & Cloning](#deployment--forking--cloning)
- [Credits & Inspiration](#credits--inspiration)

## UX

### Strategy

#### User Stories
To plan all features and functionalities of the e-shop, the agile methodology was considered. The core of the methodology is to create epics that are broken down into user stories. Each user story was additionally prioritized using MOSCOW approach. The following epics and user stories were planned:
 
<details>
<summary>EPIC 1: Preperation & Deployment</summary>

- [#1](https://github.com/brodsa/loopitoy/issues/1): As a developer I want to plan the development of the e-shop so that I can smoothly develop the web page.
- [#2](https://github.com/brodsa/loopitoy/issues/2): As a developer I want to document the webpage and the development so that the provided solution is transparent and everybody can follow the development.
- [#3](https://github.com/brodsa/loopitoy/issues/3): As a developer I want to test and validate my webpage so that I can guarantee full functionality and development according to best practice.
- [#4](https://github.com/brodsa/loopitoy/issues/4): As a developer I want to deploy the page so that I can guarantee that the web page is accessible to everyone.

</details>

<details>
<summary>EPIC 2: SEO & Marketing</summary>

- [#6](https://github.com/brodsa/loopitoy/issues/6): As a Site User I want to read delivery information so that I know what to expect regarding delivery and refund.
- [#7](https://github.com/brodsa/loopitoy/issues/7) :As a role I want to know how my date are used so that I can decide which personal detail I provide.
- [#8](https://github.com/brodsa/loopitoy/issues/8): As a Store Owner I want to send updates and new arrivals to my customers so that I can regular inform them and motivate to purchase.
- [#37](https://github.com/brodsa/loopitoy/issues/37): As a Site Owner I want to use some SEO techniques so that I can increase the chance to purchase on my e-shop. 
- [#38](https://github.com/brodsa/loopitoy/issues/38): As a Site User I want to see favicon in the browser tab so that I can easily find the e-shop in my browser.
- [#39](https://github.com/brodsa/loopitoy/issues/39): As a Site User I want to read about Terms and Conditions so that I know what to expect when selling toys.
- [#41](https://github.com/brodsa/loopitoy/issues/41): As a Site User I want to have the possibility to provide review so that I can support and make the e-shop more reliable

</details>


<details>
<summary>EPIC 3: Viewing & Navigation</summary>

- [#5](https://github.com/brodsa/loopitoy/issues/5): As a first visitor I want to quickly see what the web-page offers so that I can easily purchase or sell toys.
- [#9](https://github.com/brodsa/loopitoy/issues/9): As a Shopper I want to view a list of all toys so that I can see the whole e-shop offer and select some to purchase.
- [#10](https://github.com/brodsa/loopitoy/issues/10): As a Shopper I want to view individual toys details so that I can find the price, description, product image and quality.
- [#11](https://github.com/brodsa/loopitoy/issues/11): As a Shopper I want to quickly identify toys according to age group and toys categories so that I can easily find appropriate toys for my children.
- [#12](https://github.com/brodsa/loopitoy/issues/12): As a Shopper I want to quickly see the total of my purchases at any time so that I can avoid spending too much time.
- [#36](https://github.com/brodsa/loopitoy/issues/36): As a Site User I want to come back to home page in case I am unexpected request so that I can continue purchasing.
- [#40](https://github.com/brodsa/loopitoy/issues/40): As a User I want to have the possibility to write the site owner so that I can contact him/her in any matter.

</details>


<details>
<summary>EPIC 4: Registration & User Account</summary>

- [#13](https://github.com/brodsa/loopitoy/issues/13): As a Site User I want to easily register so that I can have a personal account.
- [#14](https://github.com/brodsa/loopitoy/issues/14): As a Site User I want to easily login and logout so that I can access my account.
- [#15](https://github.com/brodsa/loopitoy/issues/15): As a Site User I want to easily recover my password in case I forget it so that I can recover access to my account
- [#16](https://github.com/brodsa/loopitoy/issues/16): As a Site User I want to receive an email confirmation after registering so that I can verify that my account registration was successful.
- [#17](https://github.com/brodsa/loopitoy/issues/17): As a Site User I want to capability so that I can view/edit/ my personal information.
- [#24](https://github.com/brodsa/loopitoy/issues/24): As a Shopper I want to have the possibility to save my delivery information when checkout so that I do not have to fill the information several times

</details>


<details>
<summary>EPIC 5: Sorting & Searching</summary>

- [#20](https://github.com/brodsa/loopitoy/issues/20): As a Shopper I want to filter for specific toys categories so that I can easily find and see what I have searched for.
- [#21](https://github.com/brodsa/loopitoy/issues/21): As a Shopper I want to search for toys by name or description so that I can find a specific toy I would like to purchase.
- [#22](https://github.com/brodsa/loopitoy/issues/22): As a Shopper I want to easily add/delete a toy when purchasing it so that I can ensure that I select the correct toy.
</details>

<details>
<summary>EPIC 6: Purchasing & Checkout</summary>

- [#23](https://github.com/brodsa/loopitoy/issues/23): As a Shopper I want to view my shopping bag so that I can identify the total cost of my purchase and all toys I will receive.
- [#25](https://github.com/brodsa/loopitoy/issues/25): As a Shopper I want to easily enter my payment information so that I can checkout quickly and with no hassies.
- [#26](https://github.com/brodsa/loopitoy/issues/26): As a Shopper I want to feel my personal and payment Information is safe and secure so that I can confidently provide the needed information to make a purchase.
- [#27](https://github.com/brodsa/loopitoy/issues/27):  As a Shopper I want to view an order confirmation after checkout so that I can verify that I have not made any mistakes.
- [#28](https://github.com/brodsa/loopitoy/issues/28): As a Shopper I want to receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my records.
- [#29](https://github.com/brodsa/loopitoy/issues/29): As a Shopper I want to view shopping history so that I can see what I have purchased so far
 
</details>

<details>
<summary>EPIC 7: Selling</summary>

- [#30](https://github.com/brodsa/loopitoy/issues/30): As a Seller I want to provide all information about toys so that Site Owner can sell toys for me.
- [#31](https://github.com/brodsa/loopitoy/issues/31): As a Seller I want to see all sells in my user profile so that I can view sell history and the status of each sell.
- [#32](https://github.com/brodsa/loopitoy/issues/32): As a role I want to capability so that I can benefit.
</details>


<details>
<summary>EPIC 8: Admin & Store Management</summary>

- [#33](https://github.com/brodsa/loopitoy/issues/33): As a Store Owner I want to add a toy so that I can add new items to my store.
- [#34](https://github.com/brodsa/loopitoy/issues/34): As a Store Owner I want to update toy details so that I can change the information including toy status.
- [#35](https://github.com/brodsa/loopitoy/issues/35): As a Site Owner I want to delete a toy so that I can remove toys that are no longer for sale.

</details>

To manage user stories and epics, a Kanban board was created as GitHub Project, see [here](https://github.com/users/brodsa/projects/6). The board has three columns, where the user stories are categorized into groups: Todo, In progress, or Done, as shown below. ![board](./docs/board.PNG)

Each user story was prioritized and implemented in 2 weeks long iterations. The Priorities as well as Epics are shown as labels .The iterations are defined as GitHub [Milestones](https://github.com/brodsa/loopitoy/milestones). The first iterations were mainly focused on the core features to ensure MVP functionality. During the later iterations additional features were implemented. The developer is aware of the fact that there should be a mix of all type of features within one iterations. But due to the time pressure caused by sickness and family reasons, the important features for MPV were mainly implemented in first iterations while others later on.

### Scope
- Purpose: The purpose of the website is to provide a platform for users to buy and sell second-hand toys. The website aims at creating a supportive platform for the circle economy where users buy toys of a guaranteed quality to offer fun for their children with a minimum of waste and carbon footprint.
- Target Audience: The target audience includes individuals who have children around and are interested in climate change and protecting our planet for future generations. This may include parents, family members, or friends who share the same philosophy about nature protection.
- Core Functionality:
    - Purchasing & Checkout: Users can easily add toys to their shopping bags and proceed with checkout.
    - Search and Filter: Robust search and filter functionality allows users to search for toys by content, category, age, and name.
    - User profiles: Users can view order history and deliver information in personal profiles.
    - Toy Management: Site Owner can manage toys on e-shop by creating, editing, or deleting toys.



### Skeleton 
Wireframes were prepared for both mobile and desktop devices using balsamiqo program.

| Pages            | Desktop | Mobile | 
|-------------------|--------|------------------|
| Informative Pages | <img src="./docs/ux/ux_wireframe_viewing_mobile.PNG" alt="ux_viewing_mobile" width="200"/> | <img src="./docs/ux/ux_wireframe_viewing_desktop.PNG" alt="ux_viewing_desktop" width="200"/> |
| Toys Pages | <img src="./docs/ux/ux_wireframe_toys_mobile.PNG" alt="ux_toys_mobile" width="200"/> | <img src="./docs/ux/ux_wireframe_toys_desktop.PNG" alt="ux_toys_desktop" width="200"/> |
| Purchasing Pages | <img src="./docs/ux/ux_wireframe_purchase_mobile.PNG" alt="ux_purchase_mobile" width="200"/> | <img src="./docs/ux/ux_wireframe_purchase_desktop.PNG" alt="ux_purchase_desktop" width="200"/> |
| Authentication Pages | <img src="./docs/ux/ux_wireframe_authentication_mobile.PNG" alt="ux_authentication_mobile" width="200"/> | <img src="./docs/ux/ux_wireframe_authentication_desktop.PNG" alt="ux_authentication_desktop" width="200"/> |
| Profile Pages | <img src="./docs/ux/ux_wireframe_profile_mobile.PNG" alt="ux_profile_mobile" width="200"/> | <img src="./docs/ux/ux_wireframe_profile_desktop.PNG" alt="ux_profile_desktop" width="200"/> |
| Contact Page | <img src="./docs/ux/ux_wireframe_contact_mobile.PNG" alt="ux_contact_mobile" width="200"/> | <img src="./docs/ux/ux_wireframe_contact_desktop.PNG" alt="ux_contact_desktop" width="200"/> |
| Review Pages | <img src="./docs/ux/ux_wireframe_review_mobile.PNG" alt="ux_review_mobile" width="200"/> | <img src="./docs/ux/ux_wireframe_review_desktop.PNG" alt="ux_review_desktop" width="200"/> |
| Sell Pages | <img src="./docs/ux/ux_wireframe_sell_mobile.PNG" alt="ux_sell_mobile" width="200"/> | <img src="./docs/ux/ux_wireframe_sell_desktop.PNG" alt="ux_sell_desktop" width="200"/> |


### Structure 
The loopIToy project was developed using python Django framework. The project contains seven applications:
- `bag` manages content of the shopping bag, i.e. add or remove items.
- `checkout` manages secured payments using stripe.
- `home` allows to pages containing mainly information, such as landing page or different types of polices.
- `profiles` allows to save delivery info into profile and access the history orders or sells.
- `toys` manages toys that are displayed on the e-shop.
- `allauth` allows to manage authentication proccesses - default django app.
- `contact` manages contact message from the site visitors.
- `review`allows to provide review for the e-shop.

#### ERD Model
The user inputs from all forms are stored in elephantSQL cloud-based database. There are seven database tables:
- `toys_toys` stores information about each toy.
- `toys_category` contains all toy categories.
- `toys_brand` stores toys brand with homepage url.
- `checkout_order` keeps order information and delivery information.
- `checkout_orderlineitem` contains information about each toy in the order.
- `profiles_userprofile` stores information about users, mainly default delivery information.
- `auth_user` contains informtion about the user authentication - default django app.
- `contact_contact` stores contact message from site visitors.
- `review_review` stores provided reviews from visitors.

The ER Diagram shows the relations between all tables. ![ERD](./docs/ux/ux_erd.PNG)


### Surface

**Colors**

The final color palette was selected using [coolors](https://coolors.co/1c304a-b49532-30592c-74301a) online tool to reflect the colors on the landing page and to reflect the favourite children colors. The pallette consist of four colors. ![Colors](./docs/ux/ux_color.PNG) The colors were accessed by [accessible color matrix tool](https://toolness.github.io/accessible-color-matrix/). The accessible combination are depicted in the [accessibility matrix](./docs/ux/us_accessibilityPNG.PNG)

**Font**

Two pairing fonts were chosen base on the [elemnetor blog article](https://elementor.com/blog/font-pairing/). The final fonts are: Archivo Black & Roboto. Both fonts were imported from [Google Fonts](https://fonts.google.com/). 

**Image**

The final image by [Susan Holt Sumpson](https://unsplash.com/@shs521?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on the landing page was chosen on [unsplash]. Two keywords were given: playing children; to get the best suitable image for the second-hand toy e-shop.

## Features
The features of the web page were planned using Agile methodology to ensure Minimum Value Product and to address planned User Stories. The core features of this django-base webpage includes CRUD functionality for both Site Users and Site Owner, so that users can create, read, update and delete records. In additon, messages are displayed after each CRUD activity.

The sites of e-shop are categorized into several groups:
- **Landing & Informative Pages** include Landing and How it Works Pages.
- **Account & Profile Pages** include all sites related to allauth app, i.e. authentication app, or profile app.
- **Toys Pages** include all pages related to toy app, e.g. overview of toys, toy detail.
- **Purchasing Pages** include both Shopping Bag and Checkout Pages. 
- **Hidden Pages and Polices** include all error hidden pages and pages with various polices, terms and conditions.
- **Review Pages** include pages related to providing and presenting customer feedback
- **Contact Page** includes contacting form.
- **Sell Pages** include a form to sell a toy and a page with the status.

The entire web page is also designed to be responsive to ensure that the e-shop is properly displayed on different devices (e.g. a mobile, a desktop). The designed follows common best practice of e-shop development. Each site has mutual components, i.e. header with a navigation menu and footer. The mutual components ensure that the user to easily navigates through the content of the e-shop.

### Common Features
- **Header**
    - Header displays navigation menu and buttons. 
    - The navigation buttons includes logo, search field and navigation buttons for profile and shopping bag
    - On small devices the menu drops into a hamburger menu.
    - The content slightly changes depending on type of user.![Navigation](./docs/features/feature_navigation_menu.PNG)

- **Footer**
  - Footer is displayed on all pages, except the pages dedicated for user or book registration.
  - Footer contains with social media links, terms and polices, newsletter sign up link ![Footer](./docs/features/feature_footer.PNG)


### Landing and Informatiove Pages
- **Landing Page** displayes introductory text and two buttons to either proceed to purschase or sell toys. ![Landing Page](./docs/features/feature_landing_page.PNG) 

- **How It Works Page** outlines the core sell procedure and offers users to register for selling toys.![How It Works Page](./docs/features/feature_how_it_works.PNG) 

### Account & Profile Pages

The core authentication pages includes:
- **Login Page** contains a form to log in via username or email into to the platform. Moreover, a user can choose to remember the login data. ![Login](./docs/features/feature_account_login.PNG)
- **Sign Up Page** contains a form to create an account. User have to register using both username and email.![Sign Up](./docs/features/feature_account_register.PNG)
- **Log Out Page** offers user to confirm logging out from the account or stay login. ![Log Out](./docs/features/feature_account_logout.PNG)
- **My Profile Page** displayes history of user activities and form to save delivery information. Each history activity can be viewed on a separated site. ![Profile](./docs/features/features_profile.png)


### Toy Pages

- **Toys Page** presents all available toys in e-shop. Each toy is depicted in a card element showing the basic information about toy, such as name, price and categories. For Site Owner, there are two buttons in addition: Edit and Remove to edit toy information and delete toy, respectively. ![Toys](./docs/features/feature_toys.PNG)

- **Toy Detail Page** displayes all toy details including buttons to add a toy into shopping bag or to return to all toys. For Site Owner, there are two buttons for adding toy information or toy deletion. ![Toys](./docs/features/features_toy_detail.png)

- **New Toy Page** displays a form to fill out in order to create new toy card. This page is only visible for Site Owner. ![New Toy](./docs/features/features_toys_add.png)
- **Edit Toy Page** contains aform to edit the toy info. This page is only visible for Site Owner. ![Edit Toy](./docs/features/features_toys_edit.png)
- **Delete Toy Page** shows a confirmation to delete the toy from e-shop. This page is only visible for Site Owner. ![Delete Toy](./docs/features/features_toys_delete.png)


### Purchasing Pages

- **Shopping Bag Page** displays the content of the shopping bag, including toy name with price, total and delivery costs. In addition, there are two buttons to either continue shopping or to proceed checkout. ![Shopping Bag](./docs/features/feature_bag.PNG).

- **Checkout Page** shows the summary order and displays displays form to fill out delivery and billing information. There are also two buttons to either return or to complete order. ![Checkout](./docs/features/features_checkout.png).

- **Checkout - Thank You Page** shows the summary order  with delivery and billing information. User is also informed about receiving the confirmation email. In order to return to Homepage, there is a button. ![Checkout - Thank you](./docs/features/features_checkout_success.png).


### Hidden Error & Policy Pages

- **Hidden Error Pages** display the error status code, name and message. In addition, there is a button to return to the landing page. There are three pages implemented for the unexpected situations: Permission denied (`status=403`), Page not found (`status=404`), Server Error (`status=500`). The layout of all hidden pages is the same - it displayes the message code, text and button to return home. ![Hidden Page](./docs/features/feature_hidden_page.PNG).
- **Policy Pages** display information about various polices and terms, such as Privacy Policy, Return & Refund, Terms & Conditions. The layout of such pages is the same. ![Polices](./docs/features/feature_polices.PNG)



### Review Pages

- **About Page** presents the idea behind the e-shop, button to send feedback. The page also displays customer feedbacks. ![About](./docs/features/feature_review_about.PNG)
- **Add Review Page** presents review form to send user opinion. ![Add Review](./docs/features/feature_review_add.PNG)


### Contact Page
- **Contact Us Page** serves for contacting Site Owner and it displays the contact form. After sending a message a thank you toast message is displayed. ![Contact](./docs/features/features_contact.PNG)


### Sell Pages

-**Sell Toy Page** displays the form to sell the toy. User has to provide information. The toy needs to be first approved in order to be send it to the platform. ![Sell Toy](./docs/features/feature_sell.PNG)
-**Toy Status Page** shows the status of the toy that a user would like to sell. There 5 status that can be shown: 
    - OPEN - Site Owner has to first approved it. 
    - DECLAIM - the toy was not approved for e-shop. 
    - E-SHOP - the toy is on e-sho and user has to wait till it is sold.
    - SOLD - the toy was sold and user can request money.
    - PAID - the money were paid for the toy. ![Status](./docs/features/feature_sell_history.PNG)


### Future & Left Features
Two planned features related to sorting are going to be implemented in next iterations, see [#18](https://github.com/brodsa/loopitoy/issues/18) and  [#19](https://github.com/brodsa/loopitoy/issues/19). Future extentions of the e-shop includes:
- Extending the Site Owner functionality directly on the e-shop by creating Manager board. Site owner could directly managing brands, received toys, categories, etc.
- Inhancing Sell Features by including the form to request money. In the form, User can specifiy which toys he/she wants to be paid. There should be probably a new app and model that stores such information and in addition the bank data to send money.
- Login with Social Media using allauth.cocialaccount and django.contrib.site apps
- Unique Form Style and general refactoring to have all views defined as class-based view.

## Business Model
loopitoy is B2C type of e-commerce application as it sells second-hand toys. It is a platform which supports circular economy for toys. Customers can both buy and sell toys using secure single payment transactions.

Customers (target audience) are mainly parents that are aware of the environemntal impact of toy production. But at the same time, they would like to offer their kids the variate of toys to support their creativity and development. These parents wish the same for other kids. Instead of throwing the old and not used toys away, they offer them to other families. Customers might include grandparents or family friends who share the same phylosophy. 

Besides the typical e-commerce feature, to buy toys on loopitoy, users can create their accounts with delivery information to make the future purchasing more comftable. Users can also view their shopping or selling history to be well informed about their activities on e-shop. 

The advantage over other second-hand platform lies in the concept that toys are collected in one place and not distributed over the selling users. This leads to reducing delivery cost for buying users. In addition, all toys are checked for their qualities or repaired to insure that customers will get what they see on e-shop.

Users can enjoy intuitive shopping with a user-friendly and minimalistic interface that is ensure on both mobile and desktop devices. To increase the credibility of e-shop, loopitoy uses secure payments with stripe that is one of the most trusted payment gateways. 

### SEO
- A meta description and keyword tags were added to all pages of the site for SEO purposes. Both short and long keywords were selected using google search suggestions and wordtracer.
- Products descriptions were added to each toy page. However, some improvements could be conducted.
- Two files for SEO were created:  robots.txt, sitemap.xml 


### Marketing

**Social**

A fictional Facebook business page was set up for marketing purposes: 
- Increased visibility is one of the biggest advantage as Facebook is one of the most popular social media platforms.
- loopIToy can directly interact and comunicate with customers by sharing news or react on customers comments. 
- It is a opportunity to present the e-shop values related to sustainability and to educate more users about this topic
- Site Owner can immediatelly see users reacations and can adopt the marketing strategies appropriatly. ![Facebook](./docs/marketing/facebook.PNG)

**Newsletter**

A newsletter was implemented with MailChimp. The form to subscribe is visible on the footer of every page in order to increase the chance that customers will notice it. Implementing newsletter has similar advantage as having social accounts. It offers a direct communication and presenting more complex information in comparison to Facebook. Site Owner can present 
updates, promotions, or other relevant content from loopIToy.

## Testing & Validation
The results of testing and validation are presented in the separated document, see [Testing & Validation](https://github.com/brodsa/loopitoy/blob/main/README_testing.md).


### Bugs
Several bugs were releaved during the development. Bellow, all complex bugs that required more time, searching, trying to be solved:
- Filter category toys: useing category names to filter out displayed category buttons shows incorect category name. Solution: use pk of categories to filter out the displayed category. SOLVED
- Handler500: error message - (urls.E007) The custom handler500 view 'loopitoy.views.handler500' does not take the correct number of arguments (request). Solution found on stackoverflow  [Django wrong amount of arguments in custom handler](https://stackoverflow.com/questions/60507625/django-wrong-amount-of-arguments-in-custom-handler). SOLVED
- Mozila Firefox on Samsung A52: Colors and white color background are not displayed. NOT SOLVED YET

## Technologies Used
- Python
    - asgiref==3.8.1
    - boto3==1.34.120
    - botocore==1.34.120
    - crispy-bootstrap5==0.7
    - cryptography==42.0.7
    - dj-database-url==0.5.0
    - Django==3.2.25
    - django-allauth==0.53.0
    - django-countries==7.2.1
    - django-crispy-forms==1.14.0
    - django-resized==1.0.2
    - django-storages==1.14.3
    - gunicorn==20.1.0
    - jmespath==1.0.1
    - oauthlib==3.2.2
    - pillow==10.3.0
    - psycopg2==2.9.9
    - PyJWT==2.8.0
    - python3-openid==3.2.0
    - pytz==2024.1
    - requests-oauthlib==2.0.0
    - s3transfer==0.10.1
    - setuptools==70.0.0
    - sqlparse==0.5.0
    - stripe==9.12.0
    - typing_extensions==4.12.0
    - urllib3==2.2.1
- HTML was used to create templates for the webpage.
- CSS was used to style the webpage in addition to Bootstrap.
- JavaScript
- [Jinja Django Templating](https://jinja.palletsprojects.com/en/3.1.x/) was used to insert data from the database into the webpage.
- [Bootstrap 5.2.3](https://getbootstrap.com/docs/5.2/getting-started/introduction/) was used for general layout and easy adjustments.
- [AWS 3S](https://aws.amazon.com/pm/serv-s3/?gclid=CjwKCAjwmrqzBhAoEiwAXVpgorKmnL1jEmxwNvSm5OHfGKp_sMdz-ekcqdlAgms4_a9PfiEcgdvXiRoCaNMQAvD_BwE&trk=518a7bef-5b4f-4462-ad55-80e5c177f12b&sc_channel=ps&ef_id=CjwKCAjwmrqzBhAoEiwAXVpgorKmnL1jEmxwNvSm5OHfGKp_sMdz-ekcqdlAgms4_a9PfiEcgdvXiRoCaNMQAvD_BwE:G:s&s_kwcid=AL!4422!3!645186213484!e!!g!!aws%20s3!19579892800!143689755565) was used to store all static files.
- [elephantSQL](https://www.elephantsql.com/) was used as the database for the production.
- [Heroku](heroku.com) was used to deploy the webpage.
- [fontawesome.com](https://fontawesome.com/search)
- [Google Fonts]() was used to import the fonts into the style.css file.
- [Color Pallete](https://coolors.co/353c3a-ffffff-967712-f7c31f-465963) was used to select accessible colors.
- [Favicon](https://realfavicongenerator.net/) was used to generate the code and files for the webpage favicon.
- [GitHub](https://github.com/) was used to store the code and host the website.
- [Visual Studio Code](https://code.visualstudio.com/) is an IDE and was used to develop the website.
- [Balsamiq](https://balsamiq.com/wireframes/?gad=1&gclid=CjwKCAjwg-GjBhBnEiwAMUvNW8jCWKFMpgnd5PZlvwNQGIt7xJ05Fes_JeSsBSzyr7ToVpReN5VdOBoC80UQAvD_BwE) was used to create wireframes.
- [Markdown Generator](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/) was used to convert excel sheet tables to markdown tables.
- Chrome LightHouse extension  was used for validating the webpage.
- [Chrome WAVE Evaluation Tool extension](https://chromewebstore.google.com/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) was used to evaluate accessibility of the webpage.
- [Termify](https://termify.io/) was used to generate all the polices and terms.
- [mailchimp](https://us14.admin.mailchimp.com/) to get subscribe input field for Newsletter.

## Deployment & Forking & Cloning
[Visual Studio Code](https://code.visualstudio.com/) and [GitHub](https://github.com/) have been used to build the web page. Make sure you have them installed or similar programs.

### Deployment
#### Setup the workspace

The workspace should be setup as follows:
1. Open the terminal in Visual Studio Code (Navigation Menu > Terminal > New Terminal)
2. Navigate to the location, where you would like to have the repository locally
3. Clone the repository `git clone https://code.visualstudio.com/`. Once the repository is successfully cloned, the repo folder is created.
4. Open VS from the repo folder. In order to setup your virtual environment, [pyenv](https://github.com/pyenv/pyenv) and [venv](https://docs.python.org/3/library/venv.html) must be installed. setup the loval environment. Run ```python -m venv venv``` to create virtual environment and `pyenv local 3.12.0` to install python version for this application.
5. Use `.\venv\Scripts\activate` to active the virtual environment.
6. Install the dependencies from the `requirements.txt` file `pip install -r requirements.txt`
7. Set up the database key for ElephantSQL Database, see [Setup Database](#setup-database)
8. Create `env.py` file to specify environment variables     
    - `SECRET_KEY` move the django secret key from `settings.py`
    - `DATABASE_URL` assign the generated database key
    - `os.environ["DEVELOPMENT"] = "True"`
    - `os.environ["DEBUG"] = "True"`
9. Build the logic to use the ElphantSQL Database in production environment (i.e. on Heroku) and the local sqlite database when developing the application.


#### Setup Production Database

1. Login to [ElephantSQL](https://customer.elephantsql.com/instance), you see all created database instances.
2. Click on the green button 'Create New Instance' at the right top corner.
3. Fill out the form. Specify database name > Select Region > Leave the data center default > Review > Create Instance.
4. You will be redirected to the overview off all instances, click on the created database instance to see details about database.
5. Copy the URL and assign it to the environment variable `DATABASE_URL` in `env.py` and add the logic to use the URL for production environment.

#### Setup Production Environment on Heroku

1. Login to [Heroku](https://dashboard.heroku.com/apps).
2. Go to Heroku personal Dashboard. At the left top corner, select 'New' > 'Create New App'
3. Type a unique project name, i.e. loopitoy. Select a region, i.e. Europe.
4. After the Heroku app is created, navigate to the 'Settings' Tab > 'Config Vars'. Following variables were configured: `SECRET_KEY, DATABASE_URL, PORT`
4. After the Heroku app is created, go to the Deploy Tab of the app and connect the app with app GitHub repository.
5. Switch your database on local environment to production database, i.e delete `DEV` from `env.py`.
5. Make initial migrations, create super user and load the city data set in production database.
7. Create a Procfile file with the command to migrate automatically for Heroku and to start the web app.
5. Deploy the app manually. After successful deployment, click on 'Enable automatic deployments'.

#### Setup AWS S3
The AWS S3 Bucket was used to host the static files. The setup procedure includes setting up S3 Bucket and IAM Identity. Both procedures are describe below in more details:

<details>
<summary> Setup S3 Bucket</summary>

1. Login to AWS Management Console.
2. Find S3 Bucket Service in the list of Services
3. Click on Crete New Bucket Button at the top right corner.
4. Set up the general configuration as follows
    - Give the name to your bucket, e.g. loopitoy
    - Object Ownership: Choose ACLs enabled > Choose Bucket owner preferred 
    - Block Public Asses: Unchecked Block all public access > Check 'I acknowledge that the current settings might result in this bucket and the objects within becoming public.'
    - Click on Create Bucket
5. You see the created bucket in the list of your buckets.
6. Set up Bucket Setting as follows
    - Click on the created bucket in the list.
    - Click on the Properties Tab
    - Scroll down and go to Static website hosting Section: Click on Edit > Chose Enable > Fill out index.html and error.html > Click on Save changes
7. Set up Permission as follows
    - Click on the Permission Tab
    - Scroll down and Click on Cross-origin resource sharing (CORS) Section: Click on Edit > Paste the configuration > Click on Save changes
    - Go to Bucket Police Section: Click on Edit > Click on Policy Generator (Select Type of Policy: S3 Bucket Policy, Effect: Allow, Principal: *, AWS Service: Amazon S3, Actions: GetObject, ARN: copy ARN from the Bucket Policy Section ) > Click on Add Statement > Click on Generate Policy > Copy the policy > Pase the policy in the Bucket Policy Section > Add "/**" in the end of the Resource > CLick on Save changes
    - Go to Access control list (ACL) Section: Check the List for Everyone (public access) > Save Changes

</details>



<details>
<summary> Setup IAM </summary>

1. Find IAM Identity and Access Management in the list of services.
3. Create a Group:
    - Select User groups on the sidebar menu
    - Click on Create Group
    - Give the name to user group, e.g. manage-loopitoy
    - Click on Create Group
4. Create Policy 
    - Select Policy on the sidebar menu
    - Click on Create Policy > Select JSON
    - Go to Actions > Select Import Policy > AmozonS3FullAccess > Click on Import policy > Copy the ARN Code from the Bucket into the Resource list, i.e. `["arn","arn/*"]` > Click on Next > Give it name, i.e. loopitoy-policy > Add Description > Click on Create Policy
4. Attached the Policy to the User Group
    - Select User groups on the sidebar menu
    - Select the created User group, i.e. manage-loopitoy
    - Go to Permission Tab > Click on Add Permission > Select Attach Policy > Select created policy, i.e. loopitoy-policy > Click on Attach Policy
5. Create a User
    - Select User on the sidebar menu
    - Click on Create User
    - Give it name, i.e. loopitoy-staticfiles-user > Click on Next > Select the User Group, i.e. manage-loopitoy, > Next > Click on Create User
6. Generate Access Key from the selected user, i.e. lopitoy-staticfiles-user
7. Add the key into your environment variables and setup the logic and variable for using AWS in settings.py
8. Setup the Config Vars in Heroku: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Configure `AWS_USE=True`

</details>


<details>
<summary> Setup Stripe & Webhook </summary>

1. Login to Stripe or create an account if you do not have it yet.
2. Search for API Keys. Currently, the keys are located in Developers Section. Add the following keys as environment variables in env.py and heroku Confic Vars: `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`. Then, define new corresponding variables in `settings.py` such as `STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')` and `STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')`, respectively.
3. In Developers Section, go to Webhooks tabs and click on Add endpoint to generate `STRIPE_WH_SECRET`
    - Copy the url of the e-shop and insert it in the Endpoint URL input field
    - Add `checkout/wh/` to the end of the inserted url.
    - Select all events and click on Add events.
    - Finally, confirm by clicking on Add and endpoint.
4. In the Webhooks tab, click on the inserted url > Click on Reveal secret. 
5. Copy the key in your environment, i.e. assign it to the new environment variable `STRIPE_WH_SECRET`
6. Repeat the procedure to generare the secret webhook key for the production, i.e. Heroku
7. Setup the Config Vars in Heroku app.


</details>


<details>
<summary> Email Confirmation Using Gmail Account </summary>

1. Login to a Gmail account and go to settings.
2. Select Accounts and Import Tab and continue to Other Google Account settings in Change account settings.
3. Go to Security Tab and turn on Two step verification.
3. Select App Password Section and create new password.
4. Create new Config Vars in Heroku app:
    - `EMAIL_HOST_PASS`
    - `EMAIL_HOST_USER`
5. Setup environment variables in `env.py` for both production and development environment.
    - development: `EMAIL_BACKEND` and `DEFAULT_FROM_EMAIL`
    - production: `EMAIL_BACKEND`, `DEFAULT_FROM_EMAIL`, `EMAIL_USE_TLS`, `EMAIL_PORT`, `EMAIL_HOST`, `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`
</details>

### Forking
To fork the repository to propose changes or use the code, follow the steps bellow:

1. Go to the GitHub repository you would like to fork, i.e. https://github.com/brodsa/loopitoy.
2. On the right hand side at the top, click on 'Fork' button.
3. The fork repository is ready to use, after creating a full duplicate of the original repository. 
4. Follow the steps to setup workspace & Co, see [Deployment](#deployment).


### Cloning

To clone repository or to collaborate, following steps are required:

1. Go to GitHub repository you would like to clone, i.e. https://github.com/brodsa/loopitoy.
2. On the right side, click on 'Code' button.
3. Copy the provided URL.
4. Within the open terminal write, change the directory where to clone the repository and type `git clone <repository.url>`.
5. Follow the steps to setup workspace & Co, see [Deployment](#deployment).



## Credits & Acknowledgement
The website is in the shape that I though I will never manage to do. This last project was really hard to finish - not because of the technology used but because all the family and healthy issues I have been coping with since last year. Therefore, at the first place, I would like to thank to my self - as it might sounds egoistic - that I found the energy and a bit of motivation to finish this project. I hope that it will be paid off one day. I am also thankfull for support of my husband and other people from CI who responded to all my questions.

My sources for inspirations and code issues are listed bellow.
- [Django Tutorial](https://www.youtube.com/playlist?list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) by Daisy McGeer was helpful to understand the Django in general and to make development much easier.
- [Butique Ado](https://github.com/ckz8780/boutique_ado_v1) by CI and all study material provided by CI was benefitial to setup Stripe and Webhook
- [Stack Overflow: Overwrite Save](https://stackoverflow.com/questions/69365764/django-i-want-to-create-a-self-generated-code-based-on-previous-records-and-a-s)
- [Privacy Policy Generator](https://termify.io/dashboard/)