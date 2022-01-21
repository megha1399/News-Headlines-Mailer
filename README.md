# News-Headlines-Mailer

This code will help you to send top news headlines from "https://news.ycombinator.com/" via gmail.


## Run Locally

Clone the project

```bash
  git clone https://github.com/megha1399/News-Headlines-Mailer.git
```

Go to the project directory

```bash
  cd News-Headlines-Mailer
```

Install required libraries if not installed already

```bash
  pip install smtplib
  pip install email.mime
  pip install datetime
  pip install requests
  pip install beautifulsoup4
```

Update lines #31, #32 and #33 [Provide "TO", "FROM" and "PASS" values]

Run the code

```bash
  python3 hn_news_mailer.py
```
