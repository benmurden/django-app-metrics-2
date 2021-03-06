import sys

from app_metrics.backends.statsd_backend import metric
from django.core.management import BaseCommand

from app_metrics.models import MetricItem
from app_metrics.utils import get_backend


class Command(BaseCommand):
    help = "Move MetricItems from the db backend to statsd"
    requires_model_validation = True

    def handle(self, **options):
        """Move MetricItems from the db backend to statsd"""
        backend = get_backend()

        # If not using statsd, this command is a NOOP.
        if backend != 'app_metrics.backends.statsd_backend':
            sys.exit("You need to set the backend to 'statsd_backend'")

        items = MetricItem.objects.all()

        for i in items:
            metric(i.metric.slug, num=i.num)

        # Kill off our items
        items.delete()
