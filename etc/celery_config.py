from celery.schedules import crontab

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'extensions.init_celery_tasks'
)
# CELERYD_HIJACK_ROOT_LOGGER = False  # 禁用默认日志
CELERYD_TASK_LOG_FORMAT = "[%(asctime)s: %(levelname)s/%(processName)s]%(task_name)s[%(task_id)s]: %(message)s"

CELERYBEAT_SCHEDULE = {
    "each10s_task": {
        "task": 'extensions.init_celery_tasks.task_10_seconds',
        "schedule": 10,
        "args": (10, 10)
    },
    "each24hours_task": {
        "task": 'extensions.init_celery_tasks.task_24_hour',
        "schedule": crontab(hour=23),
        "args": (10, 10)
    }
}
