mkdir -p data
mkdir -p sql
mkdir -p src

# Create files inside data/
touch data/users.csv
touch data/ads.csv
touch data/interactions.csv

# Create files inside sql/
touch sql/schema.sql
touch sql/join_user_ads.sql
touch sql/ad_ctr.sql

# Create Python source files inside src/
touch src/data_preprocessing.py
touch src/feature_engineering.py
touch src/model_training.py
touch src/ranking_model.py
touch src/inference.py

# Create remaining root-level files
touch app.py
touch requirements.txt

echo "File created Successfully"