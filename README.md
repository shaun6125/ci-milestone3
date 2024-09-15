# Code Institute: Milestone Project 3 #

## Lets Cook! ##
This project has been created for my Milestone Project 3 for the Full Stack Development Diploma at The Code Institute. The purpose of the project is to create a full-stack site that allows users to manage a common dataset about a particular domain, using HTML, CSS, Javascript, Python, Flask and MongoDB.

Lets Cook! is an online cookbook for everyones favorite recipes. The aim of Lets Cook! is to provide a website where users can find and share recipes. Users will interact with the website through being able to create, read, upload and delete recipes.

My deployed project can be viewed live [here](#).

## UX ## 

### Main Aims ### 
* To create a website that acts as an online cookbook for users to find recipes from around the world.
* To create a website that provides a quick and simple way for members to create, read, upload and delete recipes within their member account.
* To make a website that uses Javascript and Python to allow the website users to interact with the website.
* To design a website that is both visually appealing and easy to navigate for the wide range of potential users.
* To create a website that provides a good user experience on mobile, tablet and desktop devices.

### User Stories ###
* I am the owner of the website, I want to promote affiliate links for the ingredients within recipes, to monitise the website.
* I am new to cooking, I want to find a range of quick, easy, challening, flavorful, healthy recipes with simple, easy cooking instructions, so I can learn to cook my own meals.
* I am a user who has submitted a recipe, I have since improved my recipe and want to update the recipe to improve it.

### The 5 Planes of UX ###
Having created the user stories so that I knew who I was designing my website for, I then followed the user centred design process to create a website that would answer the above user stories.
1.	**Strategy Plane:**
    * When addressing the strategy plane, I focused on who the website users were likely to be and the objectives the website needed to meet to attract these users.

        * Reason for the website's existence – To serve a world-wide community of home cooks allowing like-minded people to find, upload and share their favorite recipes.        
        * User demographic – the website is open to members of all ages who are likely to have a large variation in cooking ability, nutrition requirements, dietary preferences, food budget, cooking equipment etc.  The website branding therefore needs to appeal visually to all ages and genders. It must also be able to be navigated easily as the users could have a wide range of computer competency levels.
    * I researched current recipe websites (specifically allrecipes (http://allrecipes.co.uk/) and BBC Good Food (https://www.bbcgoodfood.com/)) to gather information on what these websites offer their users; the pros and cons that I liked as a user of their website and to identify the features and information they provided. This gave me ideas of how to address my user's needs but also how I could further improve my user's experience to add value to the Lets Cook! website.

2.	**Scope Plane:**
    * When addressing the scope plane, I focused on what features were to be included on the website and its key functionality to meet the user's needs. 
	    * Requirements: ability to find recipes, ability to create, upload, edit and delete recipes and the ability to share recipes with others.
        * Key features (from the user's perspective): an easy-to-use form to search for recipes that meet my needs, a simple process to join as a member, a simple process to log in to my member account, an easy-to-use form to create and upload my own recipes, an easy way of editing my recipes and a simple method to share my recipes with others.
        * CRUD functions: To achieve the above requirements and key features I needed to implement the Create, Read, Update & Delete (CRUD) functions for my database. I decided to use them in the following ways:
            1. Create: 
                * Create a new user (register account)
                * Create a new recipe (add recipe)
            2. Read:
                * To search, find and read recipes in the database
            3. Update:
                * Update a recipe (edit recipe)
            4. Delete: 
                * Delete a recipe

3. **Structure Plane:**
    * When addressing the structure plane, I focused on the journey the website would take the users on. I kept in mind the question: What is an intuitive way to navigate through the content and features?
        * How to get there? I knew that my website should include a navbar with tabs to enable users to easily navigate through the website content. There would also be buttons linked to specific parts of the website such as the 'register' form to allow users to quickly and easily access the main features.
        * I wanted some of the website such as the home page with some taster recipes and the about page to be open to all users, but for some pages like the add recipe page to be visible only to users who were logged in to their account in the website. I decided to have different tabs displaying, depending on whether or not a user was logged in. For example, a user who is already logged in doesn't want to see 'Register' or 'Login' options, so instead can see 'Logout'.
        * How will they move through the website? – user who isn't logged in. This user can see 4 pages: Home, About, Login and Register. By using this order, the user first learns about the basis of the site and can see its basic features. Finally, the user has the option of logging in or registering an account to access more website features.
        * How will they move through the website? – user who is logged in. This user can see 6 navbar tabs: Home, About, Your cookbook, Add recipe, contact and Logout. This user can access the home page, see recipes, where they can edit or delete their own recipes, add their own recipes, contact the administrator and logout of their account.

4. **Skeleton Plane:**
    * When addressing the skeleton plane, I focused on the keeping the layout design of the website familiar to the users by using a standard layout the users would be use to seeing. 
    * How to style the page? I knew that my website pages should be consistent in style and that they should use a standard page layout. I chose to use features the user would expect to see including: a navbar at the top of the page, a header title at the top of each page, a main body and a footer at the bottom of the page with social media links.

5. **Surface Plane:**
    * When addressing the surface plane, I focused on the website branding and details like the colour, fonts and images. 

        * Images – well presented meals from around the world and images of chefs making the meals to appeal to the website's users.
        * Colour scheme – I chose to use mostly black, grey and white as these are gender neutral colours that will appeal to people of all ages. They are also clean colours that will not distract from the large number of colours in recipe photos. 
        * Icons – I chose to use font awesome icons across the pages where it could aid the user's understanding and for greater visual appeal.
        * Logo – I chose to position the logo in the top center image of the website and (on the left of the navbar) as this is a something that users have to come to expect.        
        * Collapsible accordion – I chose to present the recipes in a collapsible accordion. This allows the user to see the recipe name. They can then click on the recipe they like to find the other information like ingredients and method, which they are encouraged to do with a dropdown arrow.


### **Wireframes**
Before I started coding my project, I created wireframes using Balsamiq. I created wireframes for mobile, tablet and desktop devices to decide the layout at different screen sizes. I also used the user stories to add more detail to the website to provide a better user experience. 

**Wireframes for mobile devices**
![Mobile device wireframes](#)

**Wireframes for tablet devices**
![Tablet device wireframes](#)

**Wireframes for desktop devices**
![Desktop device wireframes](#)

### **Database structure**
I started my project by getting my data structure in place first.
* The data for this project is stored in my MongoDB database within three collections as follows:

    1. Categories - this stores the recipe category options of country - eg. italian, british, american etc.
    2. Recipes - when a recipe is added by the user, it is stored in this collection along with the information about the recipe collected from the add recipe or edit recipe form.
    3. Users - when a new user registers an account, it is stored in this collection along with their username and their password that is securely stored via a hashing method.

### **Features**
Features consistent across all the different pages of my project include:

1. **Navbar**
    * The navbar has the Lets Cook! logo which, when clicked, returns the user to the home page. On the right-hand side are the navigation tabs linking to each of the pages. The navbar tabs change depending on whether or not the user is logged in, to provide a better user experience by showing them only what they need. When the user hovers over a navbar tab, the background opasity of the tab changes to provide visual feedback as to which tab they are about to click. The navbar collapses to a toggle button on tablet and mobile devices for an improved user experience on smaller screen sizes.

2. **Title**
    * Each page starts with a simple title, that explains the purpose of that page. The text colour is consistent across all pages.

3. **Footer**
    * The footer is the same colour across all pages to provide consistency in design. It includes social media links and copyright information. The footer is the normal place that a user would look for this information. The social media links open a new tab, when clicked by the user, to take them to the corresponding website.

4. **Flash messages**
    * All flash messages are the same in style, font size and colour (i chose a light blue for these to stand out from the rest of the clean design, but not too much as so to keep in line with a clean feel.). They are all full-screen width and located at the top of the page the user is on. The text is centered and large, to be easy to read. 

5. **Interactive features**
    * When the user hovers over a button, link or Javascript element such as the navbar tabs, buttons, logo, collapsible accordion, social media link icons; then the mouse cursor changes from an arrow to a pointed finger cursor to provide a visual indication to the user that they can click on this item and to encourgae them to click it.

Features on the seperate pages include:
1. **Home Page**
    * Includes a row of cards showing 6 images which highlight a taster of the variety of meals, and following these links gives a small selection of meals to view. It shows the meals being enjoyed by people, and showcases an appealing finished meal that the user can replicate from the recipes. These images are relevant to the purpose of the website and will appeal to the intended website users.

2. **Recipes Page**
    * Includes a search bar that invites the website user to search for a recipe name that they would like to find. Along with two buttons: one to perform their search and the other to reset back to the full recipe list after they have performed a search. The buttons are different colours to make it visually obvious to the user that these buttons have different purposes.
    * Includes a collapsible accordian with the recipe information. When unselected, the accordian header shows the recipe name to the user. The user is prompted to expand the collapisble with a dropdown arrow symbol. When selected the collapsible expands to provide the rest of the recipe information. A header, paragraphs and bold text elements make it easy for the user to read, find and understand the information displayed.

    **Additional features for logged in users**

     * A black delete button at the bottom of the collapsible, is displayed next to the user's own recipes. The black provides a visual warning that pressing the delete button is an action that will remove the recipe.
     * A grey edit button at the bottom of the collapsible, is displayed next to the user's own recipes. The grey fits with the colour scheme of the website and is softer than the deep black of the delete button to emphasis that this is an edit not delete option. Pressing this button opens the edit recipe form.

3. **Login page**
    * Includes a login form requiring the user to enter their username and password and then submit their information by pressing the 'login' button to access their account. 
    * Includes a link to the register page if the user doesn't already have an account to login to.
    * If the user enters an incorrect username or password, a flash message appears saying: "Incorrect username and/or password". This is a full-screen width message with an obvious light blue border at the top of the page to be really obvious to the user.
    * Both the username and password form inputs must be completed before the user can login.

4. **Register page**
    * Includes a register form requiring the user to enter a username and password and then submit their information by pressing the 'register' button to create their account. 
    * Includes a link to the login page if the user already has an account to login to.
    * If the user enters a username that already exists in the database, a flash message appears saying: "Username already exists, please try again". This is a full-screen width message with an obvious light blue border at the top of the page to be really obvious to the user.
    * The password must be between 6 and 15 characters and include only a-zA-Z0-9.
    * Both the username and password form inputs must be completed before the user can register.

5. **Profile page**
    * Includes an initial flash message welcoming the user. This is a full-screen width message with an obvious light blue border at the top of the page to be really obvious to the user.
    * Includes a profile box saying "{username's} cookbook" to personalise the profile page to that user.
    * includes the accordian for recipes from all users of the site, with editing and deletion options only available on the users own recipes.

6. **Logout**
    * Upon clicking the logout navbar tab, the user is redirected back to the login form. A flash message appears saying: "You have successfully logged out" to confirm to the user that they have logged out. This is a full-screen width message with an obvious light blue border at the top of the page to be really obvious to the user.

7. **Add recipe**
    * Includes a form that requires all the inputs to be completed before the user can add their recipe.
    * Icons next to some of the form inputs aid the user's understanding of what the field inputs mean.
    * The recipe category input is a dropdown menu for the user to quickly and easily select one of the categories available in the database.
    * One click at the end of the form via the 'add recipe' button, adds their recipe to the database. This button also has a plus icon to further improve the user experience. Upon clicking the button, the user is returned to the recipes page and a flash message saying: "Recipe successfully added" confirms that their recipe has been included in the database.
   
8. **Edit recipe**
    * Upon clicking the 'edit' button, the user is directed to the edit recipe form. This looks exactly the same as the add recipe form, so will already be familiar to the user. Furthermore, it is preloaded with the information from the original recipe. This makes it simple for the user to see what the current recipe says and make edits to the recipe a quicker process. 
    * The user has two options: a grey 'cancel' button and a black 'edit recipe' button. The grey 'cancel' button has a cross to enhance the user's understanding of this button's function. Clicking this button returns the user to the recipes page. The black 'edit recipe' button has an edit icon, again enhancing the user's understanding of the button's purpose. Clicking this button causes a flash message saying: "Recipe successfully updated" to appear.

9. **Delete recipe**
    * Clicking to delete the recipe also returns the user to the recipe page but this time with a flash message saying: "Recipe successfully deleted".

### **Future Scope**

I think that there is a lot of potential to further develop this website, which is unfortunately beyond the scope and time frame of this Milestone Project. In the future, I would like to implement the following features:

* Recipe photos to be added to the collapsible to improve the visual appeal of the website, aid the user's website experience and improve their understanding of the recipe.
* Add the ability for users to rate/review the recipes and add these customer reviews to the collapsible for each recipe.
* Add more interactive features such as video demonstrations of making the recipes. This would then open the website up to more users such as those who can't read, are blind or that cannot undertsand the English language but that could watch or listen to a video.
* Add other icons/information to the collapsible accordion such as the time needed to cook the recipe, nutritional content or the cooking skill level required to make it etc. I would then add a toggle switch for these features to the add/edit recipe forms to collect this information, store it in the database and retreive it for displaying on the collapsible.
* Add the ability for a user to reset their password.
* add affiliate links to the ingredients to monitise the website through directing the user to purchase items from a specific retailer.
* Add a feature that can auto adjust the quantities of ingredients based on the required people serving size, taking the math out of the equation for the user.

### Technologies Used ###
* HTML5 used for the .html pages
* CSS used to style the html pages.
* Javascript used to make my website interactive with the carousel and collapsible accordian.
* [jQuery](https://api.jquery.com/) javascript library used for my javascript code denoted by $ prefix on script.js.
* [Random Key Gen](https://randomkeygen.com/) to produce the secure passwords used in my project.
* [Balsamiq](https://balsamiq.com/) used to create my wireframes.
* Jinja - templating language for some of my Python code denoted by {% %}.
* [Bootstrap](https://getbootstrap.com/) for the main and mobile navbars, footer, collapsible accordian, clean template, form templates, card templates and grid layout.
* [Canva](https://www.canva.com/) used to create the image for the add a recipe image card on the profile page.
* [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) used to check the validity of my html code for all .html pages.
* [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/#validate_by_input) used to check the validity of my css code for the style.css file.
* [JSHint](https://jshint.com/) used to check the validity of my javascript code for the script.js files.
* [PEP8 Online](http://pep8online.com/) used to check the PEP8 compliance of my Python code.
* [Am I responsive](http://ami.responsivedesign.is/#) used to check the responsiveness of my design on different screen sizes and for creating the first image in this README file.
* [Google Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) used to generate Lighthouse reports on the performance of all my web pages once the project was deployed.
* [Heroku](https://www.heroku.com/what) to deploy my website.
* [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=bing&utm_campaign=mdb_bs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=415204562&msclkid=9d365b5212331e600c093b9174dbb54f) to create my database used in this project.
* [Pymongo](https://pymongo.readthedocs.io/en/stable/index.html) for getting my MongoDB database to work with my Python code.
* Flash Python microframework used to help write the Python code for this project.
* [Gitpod](https://www.gitpod.io/) to write my project code.
* [GitHub](https://github.com/) remote repository where my project is stored.
* [Font Awesome](https://fontawesome.com/) for the icons used throughout the website.

### **Testing**

## **HTML Validation**
I passed all my html code through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input).

## **CSS Validation**
I passed my css code from style.css through the [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/#validate_by_input). No errors were found.

## **Javascript Validation**
I passed my javascript code from script.js through [JSHint](https://jshint.com/). There were no errors.

## **PEP8 Validation**
I passed my Python code from app.py and env.py through [PEP8 Online](http://pep8online.com/).

## **Manual Testing of features**
The following manual tests were carried out on Microsoft Edge, Google Chrome and Mozilla Firefox:
* Social media links were clicked on to make sure that they open in a new tab.
* Navbar items were clicked on from each page to make sure that they navigate to the correct page.
* All buttons and links were clicked on to check that they take the user to the correct page.
* Clicking on the Lets Cook! logo in the navbar returns the user back to the home page.
* Checked the mouse cursor changed from an arrow to a pointed finger when the user could click/swipe on an item like buttons, links, collapsible accordian etc.
* Tried the register, log in and log out functions to ensure all data was pulling across to and from the database, and that options available to the user were specific to the session user/account holder.
* Tried the add recipe, edit recipe and delete recipe functions to ensure all data was pulling across to and from the database. 
* Tested the email function in the contact page to ensure it was connected successfully and sending emails to myself.
* Checked the responsiveness of the website across multiple devices. 

## **Problems Resolved During Testing**
The biggest problem I had during the development of the website was connecting mongodb, as the dependancies listed in the tutorial videos provided by code institute would not work for me. 
* I tried several things, and with no joy I gave up and tried to start again using postgresql. After a short time I came back and researched how to update all the dependancies and so updated all. This worked, however I was presented with another issue, this time one of my own making. The closeness of 'recipies' and 'recipe' in the app.py file had me mixing the two several times and causing big delays to the work flow.
* Being new to flask and python, learning on the project was insightful, however again due to time constraints for the project I found myself having to heavily rely on reasearching to problem solve and this reduced what I had hoped I could achieve for the overall project.

### **Deploying my project**

 I created my project using Gitpod and deployed my project using the Heroku app hosting platform.

* To deploy my wesbite I completed the following steps:

    1. Typed "pip3 freeze --local > requirements.txt" into the command terminal on my Gitpod workspace.
    2. Typed "echo web: python app.py > Procfile" into the command terminal on my Gitpod workspace.
    3. Opened the requirements.txt file to check all my dependencies were listed.
    4. Opened the Procfile and removed the blank space at the bottom of the file.
    5. Opened Heroku.
    6. Signed into my account.
    7. Created a new app with a unique name that had not already been taken (this project uses 'lets-cook-ci'). 
    8. I then selected the region closest to me: 'Europe'.
    9. Clicked the 'Create app' button.
    10. I opened the 'Settings' tab.
    11. Clicked the 'Reveal Config Variables' button.
    12. I then inputted the Config Vars name and associated value/password for the following:
        * IP
        * MONGO_DBNAME
        * MONGO_URI
        * PORT
        * SECRET_KEY
    13. Clicked the 'Deploy' tab.
    14. Selected the 'Connect to Github' button next to 'Deployment method'.
    15. Ensured my GitHub profile was displayed and then selected my GitHub repository for the project (this project is called shaun6125/ci-milestone3).
    16. Then clicked the 'Connect' button.
    17. Back on Gitpod, I committed the requirements.txt and Procfiles.
    18. I then did a Git push to push them to GitHub.
    19. Back on Heroku, I clicked the 'Enable Automatic Deployment' button.
    20. Clicked 'Deploy Branch'.
    21. Finally, I clicked on the 'View' button to view my deployed project.

### **Using My Project**

To run my project locally you can clone the project.

* To clone my project, complete the following steps:

    1. Open GitHub.
    2. Select my project repository called shaun615/ci-milestone3.
    3. Click on the green 'Code' button.
    4. Click the clipboard icon next to the url to copy the url link.
    5. Open Git Bash.
    6. Change the current working directory to the location where you want the cloned directory.
    7. Type git clone, and then paste the url link you copied in step 4.
    8. Press enter to create your local clone.

        Alternative methods of cloning my project can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

To make a copy of my project to your GitHub account, you can fork a copy of my project.

* To fork a copy of my project, complete the following steps:

    1. Log in to your GitHub account (or create a new account).
    2. Search for my repository called shaun6125/ci-milestone3.
    3. In the far right-hand corner of the screen at the top of the repository, click the 'fork' button next to the fork icon.

    Further information about forking a repository can be found [here](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).

### **Credits**
* The website is for a fictional online cookbook, the content is fictional and was created by myself.
* I used this [post](https://stackoverflow.com/questions/31575496/prevent-negative-inputs-in-form-input-type-number) to get the min="0" class for ensuring only positive numbers could be added for my numeric form input fields on the add recipe and edit recipe forms.

### Acknowledgements ###
* The Code Institute tutorial videos, especially from the 'Mini project | Putting it all together' section in the 'Backend Development' module.
* My family and friends who tested my website on their devices and provided feedback to improve my website.

### Media ###
The images used on my website are from:
* [BBC Good Food](https://www.bbcgoodfood.com/)
