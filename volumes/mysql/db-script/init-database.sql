create database `sample_app`;

grant ALTER, CREATE, CREATE TEMPORARY TABLES, DELETE, DROP, FILE, INDEX, INSERT, LOCK TABLES, SELECT, UPDATE, REFERENCES, PROCESS on *.* to app_user@localhost identified by 'AppUser123!';
grant ALTER, CREATE, CREATE TEMPORARY TABLES, DELETE, DROP, FILE, INDEX, INSERT, LOCK TABLES, SELECT, UPDATE, REFERENCES, PROCESS on *.* to app_user@'%' identified by 'AppUser123!';
grant SUPER on *.* to app_user@localhost;
