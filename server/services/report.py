""" Defines the JobGroup repository """

from models import JobGroup, db
import pandas as pd
import json


class ReportService:
    """ The service for the generating reports """

    @staticmethod
    def get():
        """ Generate a report """
        try:
            hour_log = pd.read_sql_table(
                table_name='hour_log', con=db.engine, parse_dates=['date'])
            job_group = pd.read_sql_table(
                table_name='job_group', con=db.engine)
            df = pd.merge(hour_log, job_group, how='left',
                          left_on='job_group_id', right_on='id', sort=True)
            df['amountPaid'] = df['hours_worked'].astype(
                float) * df['wage'].astype(float)
            df['payPeriod'] = df['date'].apply(
                lambda x: ReportService.generate_pay_period_json(1, 15, x.month, x.year, ) if x.day <= 15 else ReportService.generate_pay_period_json(16, 31, x.month, x.year, ))
            df = df[['payPeriod', 'employee_id', 'amountPaid']].groupby(
                ['payPeriod', 'employee_id']).sum().reset_index()
            df = df.rename(columns={'employee_id': 'employeeId'})
            df = df.sort_values(['employeeId', 'payPeriod'])
            df['amountPaid'] = '$' + df['amountPaid'].astype(str)
            json_df = json.loads(df.to_json(orient="records"))
            for item in json_df:
                item['payPeriod'] = json.loads(item['payPeriod'])
            return json_df
        except Exception as e:
            raise e

    @staticmethod
    def generate_pay_period_json(start_date, end_date, month, year):
        data = {
            "startDate": f"{year}-{month}-{start_date}",
            "endDate": f"{year}-{month}-{end_date}",
        }
        return json.dumps(data)
