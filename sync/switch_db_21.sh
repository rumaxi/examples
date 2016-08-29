#!/bin/bash

servers=( 192.168.109.31 192.168.109.32 192.168.109.33 192.168.109.34 192.168.109.35 192.168.109.36 192.168.109.37 192.168.109.38 192.168.109.39 )


command="sudo /usr/bin/swbase21"

echo "Content-type: text/html"
echo ""
cat header.html

echo "DB Switched to 21" | /usr/sbin/sendmail -v burovi@avangard.ru
echo `date`"<br>"
for server in "${servers[@]}"; do echo "--- $server ---"; ssh "$server" "$command"; echo "<br>"; done

echo '<font size="2" color="green">Успешно переключились на базу PRODUCTION MASTER</font><br>'

cat footer.html

