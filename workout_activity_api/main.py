from nutritionix_data import Nutritionix
from sheety_handler import Sheety
from datetime import datetime


input_sentence = input("Please Enter your workout activity: ")

nutri = Nutritionix()
nutri.set_data(input_sentence, 'Male', 71, 175, 30)
nutri_result = nutri.post_request()

sheety = Sheety()
for exercise in nutri_result['exercises']:
    today_date = datetime.today().strftime('%d/%m/%Y')
    today_time = datetime.today().strftime('%H:%M:%S')
    sheety.set_data(today_date, today_time, exercise['name'].title(), exercise['duration_min'], exercise['nf_calories'])
    sheety.post_request()


