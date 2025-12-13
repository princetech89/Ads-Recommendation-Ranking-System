CREATE TABLE users (
    user_id INT PRIMARY KEY,
    age INT,
    gender TEXT,
    interests TEXT,
    location TEXT
);

CREATE TABLE ads (
    ad_id INT PRIMARY KEY,
    category TEXT,
    keywords TEXT,
    cost FLOAT,
    advertiser_id INT
);

CREATE TABLE interactions (
    user_id INT,
    ad_id INT,
    clicked INT,
    impression_time TIMESTAMP
);
