#!/bin/sh


rm d1_ignore.json
rm d2_ignore.json

sed s/\"//g d1.json > d1_ignore.json
sed s/\"//g d2.json > d2_ignore.json
sed -i '/save_price/d' d1_ignore.json
sed -i '/save_price/d' d2_ignore.json
sed -i '/original_price/d' d1_ignore.json
sed -i '/original_price/d' d2_ignore.json
sed -i '/formated_date/d' d1_ignore.json
sed -i '/formated_date/d' d2_ignore.json
diff -I RE d1_ignore.json d2_ignore.json

