import joblib
import pandas as pd

def rank_ads(model, pipeline, user_row, ads_df):
    user_df = pd.concat([user_row] * len(ads_df)).reset_index(drop=True)
    final_df = pd.concat([user_df, ads_df], axis=1)

    features = pipeline.transform(final_df)
    scores = model.predict_proba(features)[:, 1]

    ads_df["score"] = scores
    return ads_df.sort_values("score", ascending=False)
