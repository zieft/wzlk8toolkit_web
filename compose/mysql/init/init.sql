#
compose/mysql/init/init.sql
Alter
user 'dbuser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON wzlk8toolkit_web.* TO
'dbuser'@'%';
FLUSH
PRIVILEGES;
