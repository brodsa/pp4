# findMEreadME

Why do we want/need to build the product

**Content**
- [UX Design](#ux-design)
- [Features](#features)
- [Testing & Validation](#testing--validation)
- [Deployment](#deployment)
- [References](#references)


# UX Design

  - User Stories
  - Wireframes
  - Structure (Code & Database)

## Fonts
The following two family fonts were chosen based on the [blog post](https://www.nichepursuits.com/best-fonts-for-blogs/).The selected fonts were taken from Google Fonts and imported into the style sheet.
- Heading font: Lato
- Body text font: Fira Sans

## Colors
The colors were selected based on the colors of the hero image. The resulting color scheme consists of 7 colors (including white and black).
![Colors](./docs/ux/ux_color.png)
The used color combination follow the following accessibility matrix.
![Color Schema](./docs/ux/ux_color_accessibility.png)

## Media

# Features
## Common Features
- Navigation Menu
    - Navigation Menu is displayed on all pages. 
    - On small devices the menu drops into a hamburger menu
    - The content depends on the type of users:
        - Unregistered User: ![Menu for visitors](./docs/features/features_navbar.png)
        - Registered User:

# Technologies
[Bootstrap 5.2.3](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
[cloudinary](https://cloudinary.com/)
[elephantSQL](https://www.elephantsql.com/)

# Testing & Validation

# Deployment
The webpage was developed using GitPod and GitHub. The webpage was deployed on [Heroku](https://www.heroku.com/platform) and can be visited [here](https://findme-readme-10d0bfb3ba28.herokuapp.com/).

## Initial Deployment
The following steps were follow to make the initial deployment:

### Local environment
1. Create env.py containing the following keys `SECRET_KEY, DATABASE_URL, CLOUDINARY_URL`,  `DEVELOPMENT`
2. In `settings.py`, import env only if env.py exists.
3. Set the following kes: 
    - `DEBUG = 'DEVELOPMENT' in os.environ` 
    - `SECRET_KEY = os.environ.get('SECRET_KEY')`
4. Set the directories for template, static and media files
5. Set up the DATABASE key for ElephantSQL Database
6. Set ALLOWED_HOST for your local and heroku apps in the list.
7. Create a Profile with the command to migrate automatically and to start the web app.

### Heroku environment
1. Login to Heroku
2. Go to Heroku personal Dashboard. In the left top, select 'New' > 'Create New App'
3. Type a unique project name, i.e. findMEreadME. Select a region, i.e. Europe.
4. After the Heroku app is created, navigate to the 'Settings' Tab > 'Config Vars'. Following variables were configured: `SECRET_KEY, DATABASE_URL, CLOUDINARY_URL`
4. After the Heroku app is created, go to the Deploy Tab of the app and connect the app with app GitHub repository.
5. Deploy the app manually. After successful deployment, click on 'Enable automatic deployments'.

### Forking the repository
To fork the repository to propose changes or use the code, follow the steps bellow:
1. Go to the GitHub repository you would like to fork.
2. On the right hand side at the top, click on 'Fork' button.
3. The fork repository is ready to use, after creating a full duplicate of the original repository. 

### Cloning the repository
To clone (the fork) repository or to collaborate, following steps are required:
1. Go to GitHub repository you would like to clone.
2. On the right side, click on 'Code' button.
3. Copy the provided URL.
4. Within the open terminal write, change the directory where to clone the repository and type `git clone <repository.url>`.

# References

