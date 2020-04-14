""" Defines the JobGroup repository """

from models import JobGroup, db
import pandas as pd


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
                          left_on='job_group_id', right_on='job_group_id', sort=True)
            df['amountpaid'] = df['hours_worked'].astype(
                float) * df['wage'].astype(float)
            df['payperiod'] = df['date'].apply(
                lambda x: f"1/{x.month}/{x.year} - 15/{x.month}/{x.year}" if x.day <= 15 else f"16/{x.month}/{x.year} - 30/{x.month}/{x.year}")
            df = df[['payperiod', 'employee_id', 'amountpaid']].groupby(
                ['payperiod', 'employee_id']).sum().reset_index()
            return df.to_json(orient="records")

        except Exception as e:
            raise e
