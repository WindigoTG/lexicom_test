# lexicom_test

```sql
UPDATE full_names 
SET status = (
    SELECT s.status 
    FROM short_names AS s 
    WHERE full_names.name LIKE s.name || '.%'
);
```


```sql
WITH temp_names AS (
    SELECT name, status 
    FROM short_names
)
UPDATE full_names AS f 
SET status = t.status 
FROM temp_names AS t 
WHERE f.name LIKE t.name || '.%';
```