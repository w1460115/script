#!/bin/bash
mysqldump -uusername -ppassword --databases blog>/var/data/backup/mysql_backup/blog_backup_`date +%Y%m%d`.sql
