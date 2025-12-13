SELECT 
    u.user_id, u.age, u.gender, u.interests,
    a.ad_id, a.category, a.keywords,
    i.clicked
FROM interactions i
JOIN users u ON i.user_id = u.user_id
JOIN ads a ON i.ad_id = a.ad_id;
