# Wave Software Development Challenge

Applicants for the Full-stack Developer role at Wave must
complete the following challenge, and submit a solution prior to the onsite
interview.

The purpose of this exercise is to create something that we can work on
together during the onsite. We do this so that you get a chance to collaborate
with Wavers during the interview in a situation where you know something better
than us (it's your code, after all!)

There isn't a hard deadline for this exercise; take as long as you need to
complete it. However, in terms of total time spent actively working on the
challenge, we ask that you not spend more than a few hours, as we value your
time and are happy to leave things open to discussion in the on-site interview.

Please use whatever programming language and framework you feel the most
comfortable with.

Feel free to email [dev.careers@waveapps.com](dev.careers@waveapps.com) if you
have any questions.

## Project Description

Imagine that this is the early days of Wave's history, and that we are prototyping a new payroll system API. A front end (that hasn't been developed yet, but will likely be a single page application) is going to use our API to achieve two goals:

1. Upload a CSV file containing data on the number of hours worked per day per employee
1. Retrieve a report detailing how much each employee should be paid in each _pay period_

All employees are paid by the hour (there are no salaried employees.) Employees belong to one of two _job groups_ which determine their wages; job group A is paid $20/hr, and job group B is paid $30/hr. Each employee is identified by a string called an "employee id" that is globally unique in our system.

Hours are tracked per employee, per day in comma-separated value files (CSV).
Each individual CSV file is known as a "time report", and will contain:

1. A header, denoting the columns in the sheet (`date`, `hours worked`,
   `employee id`, `job group`)
1. 0 or more data rows

In addition, the file name should be of the format `time-report-x.csv`,
where `x` is the ID of the time report represented as an integer. For example, `time-report-42.csv` would represent a report with an ID of `42`.

In addition, the file name of the time report should be of the format `time-report-x.csv`, where `x` is the ID of the time report. For example, `time-report-42.csv` would represent a report with an ID of `42`.

You can assume that:

1. Columns will always be in that order.
1. There will always be data in each column and the number of hours worked will always be greater than 0.
1. There will always be a well-formed header line.
1. There will always be a well-formed file name.

A sample input file named `time-report-42.csv` is included in this repo.

### What your API must do:

We've agreed to build an API with the following endpoints to serve HTTP requests:

1. An endpoint for uploading a file.

   - This file will conform to the CSV specifications outlined in the previous section.
   - Upon upload, the timekeeping information within the file must be stored to a database for archival purposes.
   - If an attempt is made to upload a file with the same report ID as a previously uploaded file, this upload should fail with an error message indicating that this is not allowed.

1. An endpoint for retrieving a payroll report structured in the following way:

   _NOTE:_ It is not the responsibility of the API to return HTML, as we will delegate the visual layout and redering to the front end. The expectation is that this API will only return JSON data.

   - Return a JSON object `payrollReport`.
   - `payrollReport` will have a single field, `employeeReports`, containing a list of objects with fields `employeeId`, `payPerdiod`, and `amountPaid`.
   - The `payPeriod` field is an object containing a date interval that is roughly biweekly. Each month has two pay periods; the _first half_ is from the 1st to the 15th inclusive, and the _second half_ is from the 16th to the end of the month, inclusive. `payPeriod` will have two fields to represent this interval: `startDate` and `endDate`.
   - Each employee should have a single object in `employeeReports` for each pay period that they have recorded hours worked. The `amountPaid` field should contain the sum of the hours worked in that pay period multiplied by the hourly rate for their job group.
   - If an employee was not paid in a specific pay period, there should not be an object in `employeeReports` for that employee + pay period combination.
   - The report should be sorted in some sensical order (e.g. sorted by employee id and then pay period start.)
   - The report should be based on all _of the data_ across _all of the uploaded time reports_, for all time.

   As an example, given the upload of a sample file with the following data:

    <table>
    <tr>
      <th>
        date
      </th>
      <th>
        hours worked
      </th>
      <th>
        employee id
      </th>
      <th>
        job group
      </th>
    </tr>
    <tr>
      <td>
        2020-01-04
      </td>
      <td>
        10
      </td>
      <td>
        1
      </td>
      <td>
        A
      </td>
    </tr>
    <tr>
      <td>
        2020-01-14
      </td>
      <td>
        5
      </td>
      <td>
        1
      </td>
      <td>
        A
      </td>
    </tr>
    <tr>
      <td>
        2020-01-20
      </td>
      <td>
        3
      </td>
      <td>
        2
      </td>
      <td>
        B
      </td>
    </tr>
    <tr>
      <td>
        2020-01-20
      </td>
      <td>
        4
      </td>
      <td>
        1
      </td>
      <td>
        A
      </td>
    </tr>
    </table>

   A request to theh report endpoint should return the following JSON response:

   ```javascript
   {
     payrollReport: {
       employeeReports: [
         {
           employeeId: 1,
           payPeriod: {
             startDate: '2020-01-01',
             endDate: '2020-01-15',
           },
           amountPaid: '$300.00',
         },
         {
           employeeId: 1,
           payPeriod: {
             startDate: '2020-01-16',
             endDate: '2020-01-31',
           },
           amountPaid: '$80.00',
         },
         {
           employeeId: 2,
           payPeriod: {
             startDate: '2020-01-16',
             endDate: '2020-01-31',
           },
           amountPaid: '$90.00',
         },
       ];
     }
   }
   ```

We consider ourselves to be language agnostic here at Wave, so feel free to use any combination of technologies you see fit to both meet the requirements and showcase your skills. We only ask that your submission:

- Is easy to set up
- Can run on either a Linux or Mac OS X developer machine
- Does not require any non open-source software

### Documentation:

Please commit the following to this `README.md`:

1. Instructions on how to build/run your application

- After downloading/cloning the repo, navigate to the root directory, create a virtual environment with python 3.5+
- You can use this command if you want `python -m venv .venv`
- run the commamnd `pip install -r requirements.txt`
- navigate to server directory `cd server`
- First you need to generate migrations. Run the following commands below
  ```
  python manage.py db init
  python manage.py db migrate
  python manage.py db upgrde
  ```
- Once this step is completed, it should generate migrations and payroll.db
- If you want to use mysql remote database then you need to download mysql client and uncomment the DB_URI in the config.py
- It will allow you to connect to my remote mysql hosting
- After the migrations, time to run the app

```
  python server.py
```

- That's it. It should run at http://127.0.0.1:3000
- I have also made a swagger for the api at http://127.0.0.1:3000/v1/spec
- There are two endpoints in the app as below
  1. POST http://127.0.0.1:3000/v1/upload - where you need to add a csv file to the `form data` with the name `file`
  2. GET http://127.0.0.1:3000/v1/report - will generate the report
- If you have any questions, feel free to reach out at vishvajit79+wave@gmail.com

1. Answers to the following questions:
   - How did you test that your implementation was correct?
     `I ran my own custom data set along with the data provided initialy. As the readme said the data will be valid and there will be no incorrect data.`
   - If this application was destined for a production environment, what would you add or change?
     `I would change a couple of things like using sepearte config for each env, writing (unit and integration tests), storing secrets for database connection in secret manager and then using IAM role based appraoch allow service to access the secret (something like aws secret manager), updating the controllers to check for valid data before storing, updating the generate report to have pagination as when there are lot of records it is bad to fetch all at once, optimize my panda query to get the json response as there is lot of room for improvement(date fixed to 1-15 and 16-31 can be changed to return proper date as each month are different), adding cicd scripts to automate the deployment process, creating libraries that can be reused like error handler that has custom error codes based on the error, returning the class name along with the method name to log the error properly, use logging services like newrelic, cloudwatch, sumologic to log all the log message, caching the report if lot of people are calling to minimize the response latency as also you dont need to call databsase every second, etc..`
   - What compromises did you have to make as a result of the time constraints of this challenge?
     `I wanted to keep it short and finish on time, so I didn't write test cases as the readme said the data provided will be valid. I wanted to improve my panda query to generate report as it will very basic. if I use some moretime than I would have optimize the query. I didn't log anything when there is an exception. I wanted to create a proper error handler that can log the location of the error, proper timestamp, etc.`

## Submission Instructions

1. Clone the repository.
1. Complete your project as described above within your local repository.
1. Ensure everything you want to commit is committed.
1. Create a git bundle: `git bundle create your_name.bundle --all`
1. Email the bundle file to [dev.careers@waveapps.com](dev.careers@waveapps.com) and CC the recruiter you have been in contact with.

## Evaluation

Evaluation of your submission will be based on the following criteria.

1. Did you follow the instructions for submission?
1. Did you complete the steps outlined in the _Documentation_ section?
1. Were models/entities and other components easily identifiable to the
   reviewer?
1. What design decisions did you make when designing your models/entities? Are
   they explained?
1. Did you separate any concerns in your application? Why or why not?
1. Does your solution use appropriate data types for the problem as described?
