# Project 3: Code-laborate (API)

This is the repository for the Fit-Friends API, Fit-Friends is a simple but fun workout/fitness sharing app, bringing people together through the shared passion for staying fit! Users can create an account and begin their journey.  Once signed in the user will be able to submit a workout of their own, sharing it with the community.  They can also update and delete any workout they post.  Outside of submitting their own workouts, a user is able to browse the already existing library of workouts by either category or by simply viewing all of the workouts.  The category browsing in the index is made easy by convenient icons signifying the type of workout.  As a user you are also able to collect your favorites by selecting the "add to favorites" option when viewing a single workout.

## Set up and Installation instructions:
1. To use this application, you simply need to ensure you are using the correct url in API Requests.
  -  Please be sure to update your application settings to communicate with this url: fit-friends-api.herokuapp.com/
2. When authenticating Tokens in API requests - use 'Token' prefix
3. Be sure to follow endpoint instructions below for correct endpoints
4. Enjoy!


### Authentication:
| Action | Method | Endpoint |
| ----------- | ----------- | ----------- |
| Sign-Up | POST | /sign-up/
| Sign-In | POST  | /sign-in/
| Change-Password |  PATCH | /change-pw/
| Sign-Out | DELETE | /delete/


### User:
| Action | Method | Endpoint |
| ----------- | ----------- | ----------- |
| Find User | GET | /one-user/:id


### Workouts: (Token Required)
| Routes | Method | Endpoint |
| ----------- | ----------- | ----------- |
| Create | POST | /workouts
| Index All | GET | /workouts
| Users Index | GET | /myworkouts
| Show | GET | /workouts/:id
| Update | PATCH | /workouts/:id
| Delete | DELETE | /workouts/:id



### Favorites: (Token Required)
| Routes | Method | Endpoint |
| ----------- | ----------- | ----------- |
| Create | POST | /favorites
| Index Favorites | GET | /favorites
| Show One | GET | /favorites/:favorite_id
| Delete | DELETE | /comments/:favorite_id

## Other Important Links & Resources Used:
**Links**
- [Fit-Friens-front-end Repo](https://github.com/MGubernick/Fit-Friends-front-end)
- [Deployed API](https://fit-friends-api.herokuapp.com/)
- [Deployed App](https://mgubernick.github.io/Fit-Friends-front-end/)

**Website Resources**

- [stackOverflow](stackOverflow.com)
- [Django Docs](https://docs.djangoproject.com/en/3.1/)
- [Django Rest_Framework Docs](https://www.django-rest-framework.org/)
- [Class Repos](https://git.generalassemb.ly/mgubernick/django-auth-template)

## Planning and Story: Development Process and Problem-Solving Strategy:

### Planning:
- The early part of my planning process was spent deciding which technologies I wanted to utilize and showcase for my capstone project.  Ultimately, I decided to take on the challenge of pairing Python/Django for the backend, API, development and Javascript/React to develop my front end application.  I then thought up a application idea that would be something my friends and I could use and enjoy on a regular basis.  This is where the idea of Fit-Friends was born!

- Once I had my idea, I created my wireframe and ERD as well as my user stories to help guide myself through the development process itself.

### CRUD Workouts:
- I began by creating the model for a workout and updating the model for user to include the user_name option. Next, I then wrote serializers for workouts to be used by the views that I also built.  After I finished writing the views, I added urls to the urls.py file so that the front end can communicate with the API. As I finished the urls and views for each CRUD function, I wrote a curl-script to test.

### CRUD Favorites:
- After completing the CRUD functionality for workouts, I moved onto creating a many to many relationship between the ueser and the workouts via a new favorites model.  After setting up the model and updating the workout model to include the new favorites key, I wrote a couple new serializers and views to handle the data needed to pair the user to the workouts and vice virsa. Finally, url endpoints for the front end to communicate with and curl-scripts to test each route.

### Problem-Solving:
- When I ran into problems, I would first spend some time looking back at lesson repos and trying to think up any ideas on my own.  If this didn't work after a little bit, I collaborated with classmates and asked them to help me out.  This is usually where I would come to a solution.  However, if that didn't work after a half hour or so, I would submit an issue and request assistance from the instructors.

## Technologies Used:
- Python
- Django
- Django Rest framework
- PostgreSQL
- Heroku

## Unsolved Problems:
- The problem that I am currently working on the solution for is being able to click on one of the oter users names (when looking at a workouts favorites) and see that user's favorite workouts.

## ERD:
![Fit-Friends ERD_v2](https://imgur.com/GHsZhCN.png "ERD")
