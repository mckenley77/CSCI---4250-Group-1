# Guide to Deploy your application
- In visual studio directly, you can right-click on the solution file and click the Publish button
- After, follow Publish -> Start -> Folder, choose your folder path, click the crete profile button, and then publish.
- You can then use your preferred hosting service's (IIS, Azure, etc) application to configure your deployment, choosing the folder you just published to.
# Guide to deploying your API:
- With FastAPI, you can deploy it directly to the FastAPI Cloud from the terminal: login with 'fastapi login', and then use 'fastapi deploy' to deploy it to the FastAPI cloud. 
- You could also run a server maually, using 'fastapi run main.py' or 'uvicorn main:app', locally. 