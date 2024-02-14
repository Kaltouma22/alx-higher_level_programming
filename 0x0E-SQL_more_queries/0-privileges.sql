-- List privileges for users user_0d_1 and user_0d_2
SELECT
    user, 
    host, 
    db, 
    table_name, 
    column_name,
    routine_name, 
    privilege_type 
FROM 
    information_schema.schema_privileges
WHERE 
    (user = 'user_0d_1' OR user = 'user_0d_2')
    AND table_schema NOT IN ('mysql', 'information_schema', 'performance_schema')
ORDER BY 
    user,
    host, 
    db, 
    table_name, 
    column_name, 
    routine_name, 
    privilege_type;
