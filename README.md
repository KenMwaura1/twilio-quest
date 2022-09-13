# Twilio Quest


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![GitHub](https://img.shields.io/github/license/KenMwaura1/twilio-quest?logo=Zoo&style=for-the-badge)

![Conda](https://img.shields.io/conda/pn/conda-forge/flask?style=for-the-badge)

This repo contains my solutions to the Twilio quest challenges. It will be updated as I continue playing.

Forked from the main [Starter-Python repo](https://github.com/twilio/starter-python)

## Setting Up the Flask app

We assume that before you begin, you will have [Python](http://www.python.org/) and [pip](http://www.pip-installer.org/en/latest/) installed on your system and available at the command line.

Before you can run this project, you will need to set three system environment variables. These are:

- `TWILIO_ACCOUNT_SID` : [Get it from your Twilio Console](https://www.twilio.com/console).
- `TWILIO_AUTH_TOKEN` : Same as above.
- `TWILIO_PHONE_NUMBER` : A Twilio number that you own, that can be used for making calls and sending messages. You can find a list of phone numbers you control (and buy another one, if necessary) [in the console](https://www.twilio.com/console/phone-numbers/incoming).

You could save them in the flask-app/settings.py file and import them in the main app.py file

OR

For Mac and Linux, environment variables can be set by opening a terminal window and typing the following three commands - replace all the characters after the `=` with values from your Twilio account:

```sh
    export TWILIO_ACCOUNT_SID=ACXXXXXXXXX
    export TWILIO_AUTH_TOKEN=XXXXXXXXX
    export TWILIO_PHONE_NUMBER=+16518675309
```

On Windows, the easiest way to set permanent environment variables (as of Windows 8) is using the `setx` command. Note that there is no `=`, just the key and value separated by a space:

```powershell
    setx TWILIO_ACCOUNT_SID ACXXXXXXXXX
    setx TWILIO_AUTH_TOKEN XXXXXXXXX
    setx TWILIO_PHONE_NUMBER +16518675309
```

## Running the application

1. Clone this repository. Navigate to the flask-app folder with the source code on your machine in a terminal window.

1. From there we recommend creating a [virtualenv](https://docs.python.org/3/library/venv.html) and activating it to avoid installing dependencies globaly on your computer.

   `python3 -m venv env`
   `source env/bin/activate`

1. Install dependencies:

   `pip install -r requirements.txt`

1. Run the web app:
   `python app.py`

1. Open the app in your [browser](http://localhost:5000/)

1. Enter your mobile number in the fields provided, and test both SMS text messages and phone calls being sent to the mobile number you provide. The web UI should look something like this:

![python guild](https://github.com/KenMwaura1/twilio-quest/blob/master/flask-app/static/twilio-app.png)

## Begin Questing!

This is but your first step into a larger world. [Return to TwilioQuest](http://quest.twilio.com) to continue your adventure. Huzzah!
