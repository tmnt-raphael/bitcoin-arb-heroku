
Heroku runs the clock process once.
- myClock.py - Scale and run clock process

Clock process schedules background task every 5 seconds.
- Uses RQ to schedule

Background task reads exchanges and saves data to postgress.
- [ ] Scale and run worker - worker listens to and performs background task

