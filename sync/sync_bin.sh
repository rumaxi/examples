#!/bin/bash


echo "Content-type: text/html"
echo ""
cat header.html

chown -R www-data:www-data /var/www/avangard.ru/bin/
chmod -R 775 /var/www/avangard.ru/bin/

#echo "bin sync" | /usr/sbin/sendmail -v burovi@avangard.ru
echo `date`"<br>"

servers=( 192.168.109.31 192.168.109.32 192.168.109.33 192.168.109.34 192.168.109.35 192.168.109.36 192.168.109.37 192.168.109.38 192.168.109.39 192.168.109.30 )

for server in "${servers[@]}"; do
                out=$(/usr/bin/rsync -rlptvogDP --exclude='robots.txt' /var/www/avangard.ru/bin/  "$server":/var/www/avangard.ru/bin/)
                echo "<h4>--- $server ---<br></h4>"
                echo "<small>$out""<br></small>"
done
	

echo '<font size="2" color="green">Готово.</font><br>'

cat footer.html

