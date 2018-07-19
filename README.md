# favorite-TV-program-scheduler
It schedules your favorite T.V. programs from multiple channels into one. Currently only works with [mncvision](https://mncvision.id/schedule/table). Can be customized for other services.

# Motivation
I don't like wasting a lot of time from my day just to scheck multiple schedules of multiple channels online to see if my show is about to air. So I decided to use more of my time to make this. It takes me about 3 hours to make this. Now, before I start my day, in only **one minute** I can check when all of my T.V. programs are going to air.

# Usage
1. Make sure all the dependencies are installed.
2. Adjust some of the constants in the python files so they suit your needs.
```python
WANTED_PROGRAMS = [
    'kevin can wait',
    'the simpsons',
    'live pd',
    'family guy'
]
URL = 'https://mncvision.id/schedule/table'
SCHEDULE_TIMEZONE = '+0700'
LOCAL_TIMEZONE = '+0900'

# Channel names (or part of channel names) must be lowercase.
CHANNEL_EXCLUSIONS = ['hd']
```
3. Open "fetch.py". After it finished running, you should see a new file called "schedule.json" with informations about your programs.
4. Open "schedule.py" to see your customized schedule. Expected output will be like:
```
+--------------------+------------------------------+---------------------+-------------+
| Showtime (GMT+9)   | Name                         | Channel             | ETA         |
|--------------------+------------------------------+---------------------+-------------|
| 19/Jul/2018 08:15  | Kevin Can Wait S2, Ep 23     | Fox Life            | in 17 hours |
| 19/Jul/2018 22:00  | Live PD: Police... S3, Ep 38 | Crime Investigation | in a day    |
| 19/Jul/2018 22:25  | Live PD: Police... S3, Ep 39 | Crime Investigation | in a day    |
| 20/Jul/2018 01:40  | Live PD: Police... S3, Ep 38 | Crime Investigation | in a day    |
| 20/Jul/2018 07:20  | Kevin Can Wait S2, Ep 23     | Fox Life            | in 2 days   |
| 21/Jul/2018 20:00  | Kevin Can Wait S2, Ep 22     | Fox Life            | in 3 days   |
| 22/Jul/2018 21:10  | The Simpsons S29, Ep 14      | FOX                 | in 4 days   |
| 23/Jul/2018 10:25  | The Simpsons S29, Ep 14      | FOX                 | in 4 days   |
| 23/Jul/2018 18:10  | The Simpsons S29, Ep 14      | FOX                 | in 5 days   |
+--------------------+------------------------------+---------------------+-------------+
```

# Dependencies
Install them using "pip install"

- https://github.com/crsmithdev/arrow
- https://github.com/gregbanks/python-tabulate
