import random

from django.shortcuts import render
from .models import *
import datetime


# Create your views here.
def index(request):
    return render(request, 'oila/index.html', {'test': 'oils'})


def report(request):
    data = []
    Entities = Entity.objects.all().order_by('Entity_id')
    oil_pipelines = oil_pipeline.objects.all()
    danger_level = danger_levels.objects.all()

    for el in Entities:
        data.append(
            {
                'entity_id': el.Entity_id,
                'this_id': el.Entity_id + 1,
                'position': el.Position,
                'area': float('%.3f' % el.area),
                'danger_level': danger_levels.objects.get(danger_id=el.danger_id).name,
                'pipeline': oil_pipeline.objects.get(oil_pipeline_id=el.pipeline_id).name
            }
        )

    return render(request, 'oila/report.html',
                  {
                      'Entities': data,
                      'all_entities': len(data),
                      'time': str(datetime.datetime.today()).split()[0],
                  })

