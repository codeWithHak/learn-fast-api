from apscheduler.schedulers.background import BackgroundScheduler
from pydantic import BaseModel, Field
from fastapi import FastAPI
from datetime import datetime
import uvicorn
from enum import Enum


app = FastAPI(title="Basic Cronjob", description="Apply basic cron job functionality using fastapi")

scheduler = BackgroundScheduler()
scheduler.start()

def send_reminder():
    print(f"Reminder is sent at: {datetime.now()}")

class Weekdays (str,Enum):
    mon = "mon"
    tue = "tue"
    wed = "wed"
    thu = "thu"
    fri = "fri"
    sat = "sat"
    sun = "sun"


class TimeInput(BaseModel):
    day:Weekdays = Field(...)
    hour:int = Field(..., ge=0, le=23)
    minute:int = Field(..., ge=0, le=59)


@app.post("/send-reminder-route")
def send_reminder_route(time:TimeInput):
    scheduler.add_job(send_reminder, trigger="cron", day_of_week=time.day.value ,hour=time.hour, minute=time.minute)
    return {"message":f"Request will be sent at {time.hour}:{time.minute} on {time.day}"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=800, reload=True)




