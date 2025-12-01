# Dev Manual
Some important terms include:
  - API, short for Application Program Interface. Allows the web page and our database to talk to each other.
  - JSON is JavaScript Object Notation, and is what is sent back and forth to/from the API to the web application. 
- To run the application, you will need the API active, and the web application active. It is currently set up for a development envrionment using localhost, so be sure to switch the frontend's API URL to the correct URL if you're actually hosting the website and API.
- Our architectural design is... Architecutral_Design.jpg, hosted in this same folder.
- Likewise, our detailed design documents are Tracker_ERD (for entity relationship flow), Student_InitialDiagram, for an early iteration of the student class, Notificiation_SimpleDesign for an overview of the (mostly unimplemented) notification system, and Maps_SimpleDiagram / Maps_LessSimpleDiagram for the data flow for the map functionality.
- We used Microsoft Planner as both our project management and issue tracking tool.

- !!! Please run main.py *normally* once when first loading the app to generate the database. Otherwise, the API will not run, and the app will not work. 
- If you're trying to add something new to the API (from the frontend) and getting an 'Unprocessable Entity' error, remember to add the JsonPropertyName wrapper to the class you're working with. We should've added all of them in beforehand, but we ended up only adding the ones that we needed/work with more frequently
- Most things should be setup for a good developer experience. Comments will be added before the project submission date. Password hashing DOES need to be added.
- For the app's functionality to  work, run 'uvicorn main:app --reload' (reload isn't necessary, but helps if you're editing it) in the TrackerAPI directory to get the API running. It *shouldn't* crash, but if it does, you can just CTRL+C and then run the command again. 
- Again, everything *should* work as expected, but things may come up once you start adding more from the API into the project. Unprocessable entity is the usual suspect. 
- If you want sample accounts for users to just see the functionality, uncomment lines 29-35 in TrackerAPI's main.py 
![A screenshot of lines 29-35 in the main.py file](LInes_To_Uncomment.png "Uncomment for Sample Users")
- Some designs may seem cobbled together from nothing. This is the case usually, as we got caught up in the messaging function for too long and had to rush the maps implementaton. Also, it was just Connor creating the maps. 
- To build, simply run the Visual Studio project and use 'uvicorn main:app' in the TrackerAPI directory to start the API up. 
- To deploy, see the deployment_guide markdown file.