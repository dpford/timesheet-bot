timesheet-bot
=============

This bot will check to see if you've submitted hours for the previous day in your Unanet timesheet.  If not, it will add the number of hours of your choosing to your project, and save it.

### Required software
* [PhantomJS](http://phantomjs.org/download.html)

### Required environment variables
* `UNANET_URL` - the main Unanet login URL, e.g. https://www7.unanet.biz/company-name/action/home
* `UNANET_USERNAME`
* `UNANET_PASSWORD`
* `UNANET_PROJECT` - the exact text inside the Project dropdown in your timesheet
* `UNANET_HOURS` - the number of hours you want entered

### Setup

1. Clone the repo on your server
2. Setup a virtual environment and install requirements.txt
3. Add the environment variables to a sourceable file
4. Copy job.sh.sample to job.sh and customize as needed
5. `crontab -e` and add something like:
```
30 9 * * 2-6 /path/to/job.sh
```
That will run the script at 9:30am local time Tues/Weds/Thurs/Fri/Sat.