We are using the OpenAI NLP engine
Using Nutritionix API: https://trackapi.nutritionix.com
to read user text on exercises he input and transform it into real fitness data
data type: exercise type, duration, calories

For example:
User input: run 10km swim 5km
The program will calculate the calories and duration according to the user profile (Age/ Weight/ Height/ Gender) 
The raw data is transformed into usable data
The data is then sent into Google Sheets with Sheety API: https://api.sheety.co/

With this app we can update on each workout we did and all is updated in Google sheets

In order to use the environment veriables create a .env file under the root directory
for example:
NUT_PASS=<your_password>
NUT_USER=<your_user_name>
NUT_API_KEY=<your_api_key>
NUT_API_ID=<your_api_id>


