I know that the weather can be obtained in ways much easier than parsing, but I wanted to practice a little in this area and wrote this parser :)
## Details what he does:
The parser pulls weather in the city of Lugansk from the Gismeteo website and sends it to telegrams according to the condition:
If at the time of parsing is before 12:00, the weather will be sent today and tomorrow, 
if later - only tomorrow.
### This parser is registered in crontab with the condition
```
0 7 * * *
0 17 * * *
```
the parser is activated every day at 7 and 17 hours.
If you want to run my parser, you will need to install requirements
```
pip install -r requirements.txt
```
and write your token and chat_id from your Telegram bot to the config.py