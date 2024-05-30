# loopitoy
## UX
- Agile Development (Strategy)
    - User Stories
    - EDR Model
    - Apps and Logic Flow
- Wireframes (Skeleton)
- Fonts & Colors (Surface)

## Features
CRUD functionality

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