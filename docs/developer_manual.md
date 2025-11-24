# Dev Manual
- !!! Please run main.py *normally* once when first loading the app to generate the database. Otherwise, the API will not run, and the app will not work. 
- If you're trying to add something new to the API (from the frontend) and getting an 'Unprocessable Entity' error, remember to add the JsonPropertyName wrapper to the class you're working with. We should've added all of them in beforehand, but we ended up only adding the ones that we needed/work with more frequently
- Most things should be setup for a good developer experience. Comments will be added before the project submission date. Password hashing DOES need to be added.
- For the app's functionality to  work, run 'uvicorn main:app --reload' (reload isn't necessary, but helps if you're editing it) in the TrackerAPI directory to get the API running. It *shouldn't* crash, but if it does, you can just CTRL+C and then run the command again. 
- Again, everything *should* work as expected, but things may come up once you start adding more from the API into the project. Unprocessable entity is the usual suspect. 
- If you want sample accounts for users to just see the functionality, uncomment lines 29-35 in TrackerAPI's main.py 
![A screenshot of lines 29-35 in the main.py file](LInes_To_Uncomment.png "Uncomment for Sample Users")