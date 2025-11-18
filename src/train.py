import mlflow

def dummy_train():
    mlflow.log_metric("accuracy", 0.95)
    print("Training placeholder logged to MLflow")

if __name__ == "__main__":
    dummy_train()
