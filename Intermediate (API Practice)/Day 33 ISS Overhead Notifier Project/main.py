from datetime import datetime
import smtplib
import requests
import time

MY_EMAIL = 'ankitpoudel.seo007@gmail.com'
MY_PASSWORD = 'IphoneX@2059'
MY_LATITUDE = 27.691709
MY_LONGITUDE = 85.299898

def is_iss_overhead():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    data = iss_response.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    iss_position = (latitude, longitude)

    if MY_LATITUDE - 5 <= iss_position[0] <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_position[0] <= MY_LATITUDE + 5:
        return True

def is_night():
    response = requests.get(url=f'https://api.sunrise-sunset.org/json?lat={MY_LATITUDE}&lng={MY_LONGITUDE}&formatted=0')
    response.raise_for_status()

    new_data = response.json()
    sunrise = int(new_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(new_data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject: Look Up\n\nThe ISS is above you in the sky.'
        )

