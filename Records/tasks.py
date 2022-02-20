from celery import shared_task
from .models import Records

@shared_task
def file_resize(records_id: int):
   Records.save_file(Records.objects.get(id=records_id))