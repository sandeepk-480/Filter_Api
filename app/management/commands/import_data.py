from django.core.management.base import BaseCommand
import pandas as pd
from app.models import Data

class Command(BaseCommand):
    help = 'Import data from Excel to MySQL'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']
        df = pd.read_csv(excel_file)

        for index, row in df.iterrows():
            ticker = row['ticker']
            date = pd.to_datetime(row['date'], format='%m/%d/%Y').strftime('%Y-%m-%d')
            revenue = row['revenue']
            gp = row['gp']
            fcf = row['fcf']
            capex = row['capex']

            data_instance = Data(ticker=ticker, date=date, revenue=revenue, gp=gp, fcf=fcf, capex=capex)
            data_instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
