UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
while read id; do
 [ -s pdp/$id.html ] && continue
 curl -s -m 30 -A "$UA" -H "Accept-Language: en-US" "https://www.airbnb.com/rooms/$id?check_in=2027-02-04&check_out=2027-02-08&adults=8&display_currency=USD" -o pdp/$id.html -w "$id %{http_code} %{size_download}\n"; sleep 1.5
done < ids.txt
echo DONE
