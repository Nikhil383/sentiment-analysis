from prefect import flow, task
import requests

@task
def check_health():
    r = requests.get("http://localhost:8000/health")
    return r.status_code == 200

@flow
def monitor():
    ok = check_health()
    print("Health OK:", ok)

if __name__ == "__main__":
    monitor()
