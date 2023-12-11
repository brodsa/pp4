# findMEreadME

findMEreadME is a unique platform to share the books and reading experience with other members. The idea is to pass the book to each other and record the members reactions as well as the journey of the book. It is for all who like a bit of adventure and reading. As a side effect, the reading becomes sustainable and the people can read more for free.

To become a member, visitor needs to register on findMEreadME. The user can create a book profile a let the book to be discovered by other members. The book profile can be edit or even deleted. Once the other member has the findMEreadME book, the 

Deployed site: [findMEreadME](https://findme-readme-10d0bfb3ba28.herokuapp.com/)

**Content**
- [UX Design](#ux-design)
- [Agile Development](#agile-development)
- [Features](#features)
- [Structure](#structure)
- [Testing & Validation](#testing--validation)
- [Deployment](#deployment)
- [References](#references)


Strategy: goals of users - epics and all stories, agile methodology
Scope: Product features
Structure: flow chart, hierarchy of the app, database schema
Skeleton: wireframes
Surface: color, text, images
Testing & Validation
Deployment
References


# UX Design

## User Stories


## Wireframes
The wireframes of the website were designed using [Balsamiq](https://balsamiq.com/wireframes/?gad=1&gclid=CjwKCAjwg-GjBhBnEiwAMUvNW8jCWKFMpgnd5PZlvwNQGIt7xJ05Fes_JeSsBSzyr7ToVpReN5VdOBoC80UQAvD_BwE). 
Two different layouts were mainly considered:
- [Desktop Wireframe](./docs/ux/wireframe_desktop.png)
- [Mobile Wireframe](./docs/ux/wireframe_mobile.png)

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
To create the website a hero picture and icons were used. The hero picture was downloaded as svg from [storyset.com](https://storyset.com/). The icons were copied as html snippet from [fontawesome.com](https://fontawesome.com/search). There are other pictures for registering the book, which were inserted by users. In addition, a book icon form [onlinewebfonts](https://www.onlinewebfonts.com/icon) was used to generate favicon.


# Agile development

# Features
## Common Features
- **Navigation Menu**
    - Navigation Menu is displayed on all pages. 
    - On small devices the menu drops into a hamburger menu.
    - The content depends on the type of users:
        - Unregistered User: ![Menu for visitors](./docs/features/features_navbar.png)
        - Registered User: ![Menu for users](./docs/features/features_navbar_user.png)

- **Footer**
  - Footer is displayed on all pages, except the pages dedicated for user or book registration.
  - Footer contains social media links as well as contact on side developer ![Footer](./docs/features/features_footer.png)


## Homepage Features
Homepage consist of 3 sections containing the features described bellow: 
- **Hero Section** contains text with a brief introduction of the platform and a thematic picture. In addition, a button allows users for immediate registration. ![Hero Section](./docs/features/features_hero.png)
- **Does this sounds familiar to you? Section** lists the motivation of users to be part of the platform. ![For you](./docs/features/features_for_you.png)
- **How it works? Page** describes the general procedure for creating a personal or book profile. User has a possibility to sin up directly from this page. ![How it works](./docs/features/features_how_it_works.png) 

## User Authentication Pages 
User Authentication pages include:
- **Login Page** contains a form to log in via username or email into to the platform. Moreover, a user can choose to remember the login data. User can refresh password, in case he/she forgot it. When user logins, the username is displayed in navigation menu. ![Login](./docs/features/features_login.png)
- **Sign Up Page** contains a form to create an account. User can register using both username or email.![Sign Up](./docs/features/features_signup.png)
- **Log Out Page** asks user to confirm logging out from the platform. ![Log Out](./docs/features/features_logout.png)

## Book Pages
Book pages include:
- **New Book Page** contains a form to register a new book. The required fields are: title, author, published year, language. The user is informed, if these form fields are not filled in or not valid (i.e. year must be between 1900 and current year). The description, image and image text fields are not required. After a successful book registration, user is redirected to the Book Key Page. ![New Book](./docs/features/features_book_registration.png)
- **Book Key Page** is the next step in registering a new book. It displays the generated unique book key. The key is used to identified the book and is used to contribute to the book journey. The page contains a button to get a template with instructions for other members. The user can proceed with the registration by clicking on the Next button, which redirects user to the Add Contribution Page. ![Book Key Page](./docs/features/features_book_key_generator.png)
- **Books Page** contains an overview of registered books. The authenticated users can see the entire content, while unregistered users have limited excess. The only visitors can view the four latest books and are asked to register if they wish to see more. ![Latest Books](./docs/features/features_book_books.png)
- **Book Page for authorized user** shows two sections: Book information and Book journey with current location information and reactions of other readers. The user who added the book is also displayed. In addition, there are two buttons to edit or delete the book. In the Book Journey Section, there buttons to add, edit or delete the contribution depending on if the user has already contributed. ![Basic Book Detail](./docs/features/features_book_detail.png) 
- **Book Page for unauthorized user** shows only basic book information, journey and the user who added the book. The deletion or edition of the book is not allowed. ![Basic Book Detail](./docs/features/features_book_detail_basic_viewer.png) 
- **Book Edit Page** contains a form to edit a registered book. The user is redirected in the Book Page after submitting the form ![Edit Book Page](./docs/features/features_book_edit.png)
- **Book Delete Confirm Page** displays a text box with the confirmation for the book deletion. ![Delete Book Page](./docs/features/features_book_delete.png)

## Contribution Pages
- **Insert Key Page** contains a form with one input field to insert book key. The form validates the user input. In case there is no match with existing keys, the user is informed about inserting an invalid key. Otherwise, the user is redirected to the book belonging to the inserted key. ![Insert Key](./docs/features/features_insert_key.png)
- **Add Contribution Page** contains a form to provide a contribution to a book. The form has two prefilled fields (i.e. Book Title and Book ID) in order to keep the form user friendly and fully functional for the desire requirements. In case user inserts invalid book key, a proper message appears on the top of the form. After inserting validate inputs, the user can finish the book registration by clicking on the Save button, which redirects user on the Latest Book Page ![Book Add Contribution](./docs/features/features_book_add_contribution.png)
- **Contribution Edit Page** contains a form to edit a book contribution. After saving the form, the user is redirected to the Books Page. ![Edit Contribution](./docs/features/features_contribution_edit.png)
- **Contribution Delete Confirm Page** displays a text box with the confirmation for the contribution deletion. ![Delete Contribution Page](./docs/features/features_contribution_delete.png)


## Contact Pages
- **Contact Page** contains a form to contact the developer. The form requires to fill in all form fields for successful sending. After the message is sent, the user is redirected to the Thank You Page. ![Contact Page](./docs/features/features_contact.png)
- **Thank You Page** displays the thank you message for contacting and a button to come back to the homepage. ![Thank You Page](./docs/features/features_contact_thank_you.png)


## Hidden Pages
- **403 Unauthorized Actions** informs the user in case of conducting unauthorized actions. The user can use the Home Button to return to the homepage. ![403 Error](./docs/features/features_error_403.png)
- **404 Page Not Found** informs the user in case of requesting invalid URL. The user can use the Home Button to return to the homepage. ![404 Error](./docs/features/features_error_404.png)
- **505 Server Error** informs the user in case of unexpected error occurs. The user can use the Home Button to return to the homepage.
- **Error Invalid Contribution** informs the user in case of contributing to the book the user has already contributed. The user can use the Home Button to return to the homepage. ![Error Invalid Contribution](./docs/features/features_error_invalid_contribution.png)

## Future & Left Features
- Successful Registration: The user is redirected to homepage and informed via displayed username in the navigation bar as this is by default. - changed acceptance criteria
- Overview of filled in information in the form to register a new book - next iteration - not needed for MVP. - changed acceptance criteria


## Added Features - goes in Agile
new feature: Validation of user input in form: check the year, check the length of description field, same book for the one user.

member area should be in drop down


# Structures
## Database model
- book
- contributionBook

## Webpage structure



# Technologies
- [Bootstrap 5.2.3](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
- [cloudinary](https://cloudinary.com/)
- [elephantSQL](https://www.elephantsql.com/)

# Testing & Validation (Manual Testing)
  - Responsivness Testing
  - Browser Compatibility Testing
  - User Stories Testing
  - Features Testing
  - Bug resolved and unresolved
  - Code Validation
  - Lighthouse testing outcomes

# Deployment
The webpage was developed using GitPod and GitHub. The webpage was deployed on [Heroku](https://www.heroku.com/platform) and can be visited [here](https://findme-readme-10d0bfb3ba28.herokuapp.com/).

## Initial Deployment
The following steps were follow to make the initial deployment:

### Local (development) environment
1. Create env.py containing the following keys:
    - `SECRET_KEY` 
    - `DATABASE_URL`
    - `CLOUDINARY_URL`
    - `DEVELOPMENT`
2. In `settings.py`, import env only if env.py exists and set the following keys: 
    - `DEBUG = 'DEBUG' in os.environ` 
    - `SECRET_KEY = os.environ.get('SECRET_KEY')`
4. Set the directories for template, static and media files.
5. Set up the DATABASE key for ElephantSQL Database
6. Set ALLOWED_HOST for your local and heroku apps in the list.
7. Create a Profile with the command to migrate automatically for Heroku and to start the web app.
8. Make initial migrations, create super user and load the city data set in development database.

### Heroku (production) environment
1. Login to Heroku
2. Go to Heroku personal Dashboard. In the left top, select 'New' > 'Create New App'
3. Type a unique project name, i.e. findMEreadME. Select a region, i.e. Europe.
4. After the Heroku app is created, navigate to the 'Settings' Tab > 'Config Vars'. Following variables were configured: `SECRET_KEY, DATABASE_URL, CLOUDINARY_URL`, `PORT`
4. After the Heroku app is created, go to the Deploy Tab of the app and connect the app with app GitHub repository.
5. Make initial migrations, create super user and load the city data set in production database.
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
5. Install all dependencies via `pip install -r requirements.tx` in the terminal.
6. Set up environmental variables in newly `env.py`, see Section (#local-environment).
7. Set up and start django app.

# References
- [QR code generator](https://qr.io/?gad_source=1&gclid=CjwKCAiAu9yqBhBmEiwAHTx5p7HcvWOK17qLT71iNrkXzWktj-C4jD5FImtELn35-3DKgfMNTSjWxxoCTZYQAvD_BwE)
- [storyset.com](https://storyset.com/)
- [fontawesome.com](https://fontawesome.com/search)
- [Google Fonts]() was used to import the fonts into the style.css file.
- [Color Pallete](https://coolors.co/353c3a-ffffff-967712-f7c31f-465963) was used to select accessible colors.
- [Favicon](https://realfavicongenerator.net/) was used to generate the code and files for the webpage favicon.
- [GitHub](https://github.com/) was used to store the code and host the website.
- [Gitpod](https://www.gitpod.io/) is an IDE and was used to develop the website.
- [Mockup Generator](https://techsini.com/multi-mockup/?url=http://www.example.com) was used to generate the mockup for README.
- [Balsamiq](https://balsamiq.com/wireframes/?gad=1&gclid=CjwKCAjwg-GjBhBnEiwAMUvNW8jCWKFMpgnd5PZlvwNQGIt7xJ05Fes_JeSsBSzyr7ToVpReN5VdOBoC80UQAvD_BwE) was used to create wireframes.
- [Markdown Generator](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/)

# Credits
- [Stackoverflow]
- [django docu]
- [daisy tutorial]
