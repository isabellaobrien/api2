# API

Take a look at the deployed api: [api](https://reading-media-api-9661e3dfdf56.herokuapp.com/)

## Api testing 

| action | expected behaviour | pass/fail |
|--------|--------------------|-----------|
| Enter the url in browser | the user should see this welcome message - "message": "Welcome to my django rest framework API!" | pass |
| Enter url/profiles | the user should see a list of user profiles, each profile should have these fields: "Id", "owner", "name”, "about_me", “image”, “created_at”, “updated_at”, “is_owner”, “following_id”, “story_count”, “followers_count”, following_count”. | pass |
| As a logged in user enter url/profiles/your profile id | you should be able to edit these fields: “name”, “about_me”, “image”. | pass |
| Enter url/stories | the user should see a list of user stories, each story should have these fields: "Id", "owner", “created_at”, “updated_at”, “title”, “content”, “description”, “is_owner”, ”profile_id”, “profile_image”, “like_id”, “likes_count”, “comments_count”, “save_id”, “save_count”. | pass |
| Enter url/stories as a logged in user | you should be able to create a story via the form. | pass |
| As a logged in user enter url/stories/your story id | you should be able to edit these fields: “title”, “content”, “description”. You should also be able to delete the story. | pass |
| Enter url/likes | The user should see the list of like instances on the stories. Each instance should have these fields: "Id", "owner", “created_at”, “story”. | pass |
| Enter url/likes as a logged in user | you should be able to create a like instance via the form. | pass |
| Try to create multiple like instances on a story | you should see this error message -  "detail": "duplicate like" | pass |
| As a logged in user enter url/likes/your like id | you should be able to delete the like instance. | pass |
| Enter url/comments | the user should see a list of user comments, each comment should have these fields: "Id", "owner", ”profile_id”, “profile_image”,  “content”, “created_at”, “updated_at”, “is_owner”, “story”, “comment_like_id”, “comment_likes_count”, “comment_reply_count”. | pass |
| Enter url/comments as a logged in user | you should be able to create a comment via the form. | pass |
| As a logged in user enter url/comments/your comment id | you should be able to edit these fields: “content”.You should also be able to delete the comment. | pass |
| Enter url/comment_likes | The user should see the list of like instances on the comments. Each instance should have these fields: "Id", "owner", “created_at”, “comment”. | pass |
| Enter url/comment_likes as a logged in user | you should be able to create a like instance on a comment via the form. | pass |
| Try to create multiple like instances on a comment | you should see this error message - "detail": "duplicate like" | pass |
| As a logged in user enter url/comment_likes/your comment like id | you should be able to delete the comment like instance. | pass |
| Enter url/replies | the user should see a list of user replies to comments , each reply should have these fields: "Id", "owner", ”profile_id”, “profile_image”,  “content”, “created_at”, “updated_at”, “is_owner”, “comment”, “reply_like_id”, “reply_likes_count”. | pass |
| Enter url/replies as a logged in user | you should be able to create a reply via the form. | pass |
| As a logged in user enter url/replies/your reply id | you should be able to edit these fields: “content”.You should also be able to delete the reply. | pass |
| Enter url/reply_likes | The user should see the list of like instances on the replies. Each instance should have these fields: "Id", "owner", “created_at”, “reply”. | pass |
| Enter url/reply_likes as a logged in user | you should be able to create a like instance on a reply  instance via the form. | pass |
| Try to create multiple like instances on a reply | you should see this error message - "detail": "duplicate like" | pass |
| As a logged in user enter url/reply_likes/your reply like id | you should be able to delete the reply like instance. | pass |
| Enter url/saves | The user should see the list of save instances on the stories. Each instance should have these fields: "Id", "owner", “created_at”, “story”. | pass|
| Enter url/saves as a logged in user | you should be able to create a save instance via the form. | pass |
| Try to create multiple save instances on a story | you should see this error message - "detail": "duplicate save" | pass |
| As a logged in user enter url/saves/your save id | you should be able to delete the save instance. | pass |
| Enter url/followers | the user should see a list of user follower instances, each follower instance should have these fields: "Id", "owner", “created_at”, “followed_name”, “followed”. | pass |
| Enter url/followers as a logged in user | you should be able to create a follow instance via the form. | pass |
| Try to create multiple save instances on a story | you should see this error message - "detail": "already following" | pass |
| As a logged in user enter url/followers/your follower id | You should also be able to delete the follower instance. | pass |
| Enter incorrect url pattern | you should see error 404(page not found) | pass |

I’ve created automated tests for all the api models. The tests for each app are stored in the test.py file. The tests  are run by entering “python manage.py test” in the terminal.

![api tests](./assets/api%20tests.png)

## API Deployment
* I made sure the libraries used were stored in the requirements.txt file.
* I navigated to heroku, I logged in and I clicked on "create an app", I named the app and selected my region.
* I navigated to the settings and added the config vars I needed. (ALLOWED_HOSTS, CLIENT_ORIGIN, CLIENT_ORIGIN_DEV, CLOUDINARY_URL, DATABASE_URL, DISABLE_COLLECTSTATIC, SECRET_KEY)
* I then navigated to the deploy tab, connected my heroku project to my github repository.
* I then manually deploy my project.