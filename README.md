# API

Take a look at the deployed api: [api](https://reading-media-api-9661e3dfdf56.herokuapp.com/)

## Api testing 

| action | expected behaviour | pass/fail |
|--------|--------------------|-----------|
| Enter the url in browser | the user should see this welcome message - "message": "Welcome to my django rest framework API!" | pass |
| Enter url/profiles | the user should see a list of user profiles, each profile should have these fields: "id", "owner", "name”, "about_me", “image”, “created_at”, “updated_at”, “is_owner”, “following_id”, “story_count”, “followers_count”, following_count”. | pass |
| Enter url/stories | the user should see a list of user stories, each story should have these fields: "id", "owner", “created_at”, “updated_at”, “title”, “content”, “description”, “is_owner”, ”profile_id”, “profile_image”, “like_id”, “likes_count”, “comments_count”, “save_id”, “save_count”. | pass |
| Enter url/likes | The user should see the list of like instances on the stories. Each instance should have these fields: "id", "owner", “created_at”, “story”. | pass |
| Enter url/comments | the user should see a list of user comments, each comment should have these fields: "id", "owner", ”profile_id”, “profile_image”,  “content”, “created_at”, “updated_at”, “is_owner”, “story”, “comment_like_id”, “comment_likes_count”, “comment_reply_count”. | pass |
|
| Enter url/comment_likes | The user should see the list of like instances on the comments. Each instance should have these fields: "id", "owner", “created_at”, “comment”. | pass |
| Enter url/replies | the user should see a list of user replies to comments , each reply should have these fields: "id", "owner", ”profile_id”, “profile_image”,  “content”, “created_at”, “updated_at”, “is_owner”, “comment”, “reply_like_id”, “reply_likes_count”. | pass |
| Enter url/reply_likes | The user should see the list of like instances on the replies. Each instance should have these fields: "id", "owner", “created_at”, “reply”. | pass |
| Enter url/saves | The user should see the list of save instances on the stories. Each instance should have these fields: "id", "owner", “created_at”, “story”. | pass |
| Enter url/followers | the user should see a list of user follower instances, each follower instance should have these fields: "id", "owner", “created_at”, “followed_name”, “followed”. | pass |
| Enter incorrect url pattern | you should see error 404 (page not found) | pass |

I’ve created automated tests for all the api models. The tests for each app are stored in the test.py file. The tests  are run by entering “python manage.py test” in the terminal.

![api tests](./assets/api%20tests.png)

## API Deployment
* I made sure the libraries used were stored in the requirements.txt file.
* I navigated to heroku, I logged in and I clicked on "create an app", I named the app and selected my region.
* I navigated to the settings and added the config vars I needed. (ALLOWED_HOSTS, CLIENT_ORIGIN, CLIENT_ORIGIN_DEV, CLOUDINARY_URL, DATABASE_URL, DISABLE_COLLECTSTATIC, SECRET_KEY)
* I then navigated to the deploy tab, connected my heroku project to my github repository.
* I then manually deploy my project.
