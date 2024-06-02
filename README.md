# loopitoy
## UX
- Agile Development (Strategy)
    - User Stories
    - EDR Model
    - Apps and Logic Flow
- Wireframes (Skeleton)
- Images
The final image by [Susan Holt Sumpson](https://unsplash.com/@shs521?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on the landing page was chosen on [unsplash]. Two keywords were given: playing children; to get the best suitable image for the second-hand toy e-shop.

- Fonts & Colors (Surface)

## Features
The features of the web page were planned using Agile methodology to ensure Minimum Value Product and to address planned User Stories. The core features of this django-base webpage includes CRUD functionality for both Site Users and Site Owner, so that users can create, read, update and delete records.

The sites of e-shop are categorized into severel groups:
- **Landing & Informative Pages** includes Landing and How it Works Pages.


The entire web page is also designed to be responsive to ensure that the e-shop is properly displayed on different devices (e.g. a mobile, a desktop). The designed follows commaon best practice of e-shop development. Each site has mutual components, i.e. header with a navigation menu and footer. The mutual components ensure that the user to easily navigates through the content of the e-shop.

## Common Features
- **Header**
    - Header displays navigation menu and buttons. 
    - The navigation buttons includes logo, search field and navigation buttons for profile and shopping bag
    - On small devices the menu drops into a hamburger menu.
    - The content sligthly changes depending on type of user.![Navigation](./docs/features/feature_navigation_menu.png)

- **Footer**
  - Footer is displayed on all pages, except the pages dedicated for user or book registration.
  - Footer contains with social media links, terms and polices, newsletter sugnup link ![Footer](./docs/features/feature_footer.png)


## Landing and Informatiove Pages
- **Landing Page** displayes introductory text and two buttons to either proceed to purschase or sell toys. ![Landing Page](./docs/features/feature_landing_page.PNG) 

- **How It Works Page** outlines the core sell procedure and offers users to register for selling toys.![How It Works Page](./docs/features/feature_how_it_works.PNG) 



### Future & Left Features
- Contact Us with the form and contact informations
- About Us

## Business Model
- project goals
- purpose and value to users and Busnisess
- target audiance - how their needs are addressed by the application
- map project goals to user stories

### SEO
- SEO (keywords, robots.txt, sitemap.xml)

### Marketing
- Social
- Newsletter

## Testing & Validation

### Bugs

## Technologies Used
[Accessible color palette builder](https://toolness.github.io/accessible-color-matrix/)
[Webp Converer](https://ezgif.com/png-to-webp?err=expired)

## Deployment & Forking & Cloning
[Visual Studio Code](https://code.visualstudio.com/) and [GitHub](https://github.com/) have been used to build the web page. Make sure you have them installed.

### Setup the workspace
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
    - `os.environ["DEV"] = "True"`
    - `os.environ["DEBUG"] = "True"`
9. Build the logic to use the ElphantSQL Database in production environment (i.e. on Heroku) and the local sqlite database when developing the application.


### Setup Production Database
1. Login to [ElephantSQL](https://customer.elephantsql.com/instance), you see all created database instances.
2. Click on the green button 'Create New Instance' at the rigt top corner.
3. Fill out the form. Specify database name > Select Region > Leave the data center default > Review > Create Instance.
4. You will be redirected to the overview off all instaces, click on the created database instance to see details about database.
5. Copy the URL and assign it to the environment variable `DATABASE_URL` in `env.py`

### Setup Production Environment on Heroku
1. Login to [Heroku](https://dashboard.heroku.com/apps).
2. Go to Heroku personal Dashboard. At the left top corner, select 'New' > 'Create New App'
3. Type a unique project name, i.e. loopitoy. Select a region, i.e. Europe.
4. After the Heroku app is created, navigate to the 'Settings' Tab > 'Config Vars'. Following variables were configured: `SECRET_KEY, DATABASE_URL, PORT`
4. After the Heroku app is created, go to the Deploy Tab of the app and connect the app with app GitHub repository.
5. Switch your database on local environment to production database, i.e delete `DEV` from `env.py`.
5. Make initial migrations, create super user and load the city data set in production database.
7. Create a Procfile file with the command to migrate automatically for Heroku and to start the web app.
5. Deploy the app manually. After successful deployment, click on 'Enable automatic deployments'.

### Setup AWS S3


### Setup Stripe & Webhook


### Forking

### Cloning


### Credits & Inspiration
- [Django Tutorial](https://www.youtube.com/playlist?list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) by Daisy 
- [Butique Ado](https://github.com/ckz8780/boutique_ado_v1) by CI
