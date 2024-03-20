from rest_framework import generics
from app.models import Data
from app.serializers import DataSerializer
from datetime import datetime, timedelta


class DataList(generics.ListAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.order_by('date')

    def get_queryset(self):
        queryset = Data.objects.all()
        ticker = self.request.query_params.get('ticker')
        columns = self.request.query_params.get('column')
        period = self.request.query_params.get('period')
        
        if ticker:
            queryset = queryset.filter(ticker=ticker)
        
        if columns:
            columns_list = columns.split(',')
            self.serializer_class.Meta.fields = columns_list
            queryset = queryset.values(*columns_list)
        else:
            self.serializer_class.Meta.fields = '__all__'

        if period:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=365*int(period.split('y')[0]))
            queryset = queryset.filter(date__gte=start_date, date__lte=end_date)

        return queryset
