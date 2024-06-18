-- This script creates a database for hbtn_0d_2
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
SET @user_exists := (SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost');
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
END IF;
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGE
