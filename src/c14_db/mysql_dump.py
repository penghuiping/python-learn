import os;
import shutil;
import time;

mysql_home = "mysql_home";
mysql_username = "mysql_username";
mysql_password = "mysql_password";
mysql_database = "mysql_database";

basepath = "basepath";
now = time.strftime("%Y%m%d%H%M%S");

basepath = basepath + "/" + now;

mysql_cmd = "{}/mysqldump -u{} -p{} {}>{}/{}.sql".format(mysql_home, mysql_username, mysql_password, mysql_database,
                                                         basepath, mysql_database);

print(mysql_cmd);
