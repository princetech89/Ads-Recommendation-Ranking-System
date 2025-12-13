import pandas as pd
import joblib
from src.ranking_model import rank_ads

def recommend_ads(user_id, k=5):
    users = pd.read_csv("data/users.csv")
    ads = pd.read_csv("data/ads.csv")

    user_row = users[users["user_id"] == user_id].reset_index(drop=True)

    model = joblib.load("lr_model.pkl")
    pipeline = joblib.load("feature_pipeline.pkl")

    ranked = rank_ads(model, pipeline, user_row, ads)
    return ranked.head(k)

if __name__ == "__main__":
    print(recommend_ads(user_id=1, k=5))
