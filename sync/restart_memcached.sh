#!/bin/bash

servers=( 192.168.109.31 192.168.109.32 192.168.109.33 192.168.109.34 192.168.109.35 192.168.109.36 192.168.109.37 192.168.109.38 192.168.109.39 )

command="sudo /usr/sbin/service memcached restart; 
	 sudo /usr/bin/pkill memcached
	 rm -rf /var/www/avangard.ru/bitrix/managed_cache/MYSQL/*; 
   	 rm -rf /var/www/avangard.ru/bitrix/cache/*;
	 rm -rf /var/www/corporate.avangard.ru/bitrix/managed_cache/MYSQL/*; 
   	 rm -rf /var/www/corporate.avangard.ru/bitrix/cache/*;
	 rm -rf /var/www/cards.avangard.ru/bitrix/managed_cache/MYSQL/*; 
   	 rm -rf /var/www/cards.avangard.ru/bitrix/cache/*;
"

echo "Content-type: text/html"
echo ""
cat header.html

#echo "Cache cleared" | /usr/sbin/sendmail -v burovi@avangard.ru
echo `date`"<br>"
echo '<font size="2" color="green">Начало процесса очистки кешей сайтов...</font><br>'
for server in "${servers[@]}"; do 
	out=`ssh "$server" "$command"`; 
	echo "$server :<br>";
	echo "$out <br>"
done
echo '<font size="2" color="green">Готово.</font><br>'

cat footer.html
