RuleParameterMaster.objects.filter(name__in=["URINE_CREATININE", "URIN_COTININE"]).update(data_type=RuleParameterMaster.DATA_TYPE_STRING)
