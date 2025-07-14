from apscheduler.schedulers.blocking import BlockingScheduler

def my_ai_job():
    print("My AI task is running...")

scheduler = BlockingScheduler()
scheduler.add_job(my_ai_job, 'cron', hour=14, minute=2)
scheduler.start()
