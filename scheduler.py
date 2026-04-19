import schedule
import time
from runner import main

def run_job() -> None:
    main()

def start_sceduler() -> None:
    schedule.every().monday.at("11:00").do(run_job)
    schedule.every().tuesday.at("11:00").do(run_job)
    schedule.every().wednesday.at("11:00").do(run_job)
    schedule.every().thursday.at("11:00").do(run_job)
    schedule.every().friday.at("11:00").do(run_job)

    print("Scheduler started. Waiting for the next run...")

    while True:
        schedule.run_pending()
        time.sleep(1)