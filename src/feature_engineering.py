import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def build_feature_pipeline():
    # Categorical & text features
    categorical = ["gender", "category"]
    text_features = ["interests", "keywords"]

    # Define the transformers
    transformer = ColumnTransformer([
        ("cat", OneHotEncoder(), categorical),
        ("interests", TfidfVectorizer(max_features=20), "interests"),
        ("keywords", TfidfVectorizer(max_features=20), "keywords"),
    ], remainder="passthrough")

    return transformer


def prepare_features(df):
    # Target variable
    y = df["clicked"]

    # Drop columns we do NOT use for training
    X = df.drop(
        columns=[
            "clicked", 
            "impression_time", 
            "location", 
            "user_id", 
            "ad_id"
        ],
        errors="ignore"
    )

    # Build pipeline and transform data
    pipeline = build_feature_pipeline()
    X_transformed = pipeline.fit_transform(X)

    return X_transformed, y, pipeline
