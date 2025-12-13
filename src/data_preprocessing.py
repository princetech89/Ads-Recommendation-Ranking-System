import pandas as pd

def load_data():
    users = pd.read_csv("data/users.csv")
    ads = pd.read_csv("data/ads.csv")
    interactions = pd.read_csv("data/interactions.csv")

    df = interactions.merge(users, on="user_id").merge(ads, on="ad_id")

    # REMOVE COLUMNS THAT SHOULD NOT BE FEATURES
    drop_cols = ["impression_time", "user_id", "ad_id", "location"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns])

    return df
