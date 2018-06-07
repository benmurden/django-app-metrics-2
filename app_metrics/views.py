from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def metric_report_view(request):
    return render(request, 'app_metrics/reports.html')
