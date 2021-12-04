import random

from django.shortcuts import render
from .models import *
import datetime


# Create your views here.
def index(request):
    # make_data()
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


def make_data():
    oil_pipeline_names = [
        'ПНПС Тулун – Транснефть',
        'НПС-2 (Тайшет - Сковородино ВСТО-1) – Транснефть',
        'НПС Лугинецкая – Томскнефть',
        'ЛПДС Южный Балык – Транснефть',
        'НПС Сатарино – Транснефть',
        'НПС Кучиминская – Транснефть'
    ]

    # for i in range(0, 10):
    #     Entity(
    #         Entity_id=i,
    #         Position="Polygon(",
    #         create_time=datetime.datetime.now(),
    #         danger_id=random.randint(0, 3),
    #         area=random.uniform(0.01, 3.5),
    #         status_id=0,
    #         pipeline_id=random.randint(0, 6)
    #     ).save()

    for i in range(0, 6):
        oil_pipeline(
            oil_pipeline_id=i,
            name=oil_pipeline_names[i]
        ).save()

    danger_levels(
        danger_id=0,
        name='средняя'
    ).save()

    danger_levels(
        danger_id=1,
        name='высокая'
    ).save()

    danger_levels(
        danger_id=2,
        name='критично высокая'
    ).save()
