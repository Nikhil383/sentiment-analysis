import pandas as pd
from sklearn.model_selection import train_test_split

def get_sample_dataset():
    data = [
        ("I love this!", 1),
        ("Terrible experience.", 0),
        ("Amazing product!", 1),
        ("Do not buy!", 0),
    ]
    return pd.DataFrame(data, columns=["text", "label"])

def prepare_split():
    df = get_sample_dataset()
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    return train, test
