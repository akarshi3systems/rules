RuleParameterMaster.objects.filter(name__in=["URINE_CREATININE", "URIN_COTININE"]).update(data_type=RuleParameterMaster.DATA_TYPE_STRING)
import os
from django.conf import settings
from rule_engine.models import RecordVersion, RuleParameterMaster
from powerai_datamd.scripts.rule_engine_helper import setup_mapping_files




path = os.path.join(settings.BASE_DIR, "configs/rule_engine", "BALIC", "mapping.csv")
RecordVersion.objects.all().delete()
setup_mapping_files("BALIC", path)
