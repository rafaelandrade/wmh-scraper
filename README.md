
<h1 align="center"> <img src="https://w7.pngwing.com/pngs/307/624/png-transparent-computer-icons-house-home-icon-angle-text-logo.png" width="30">
 WhereIsMyHome - Scraper </h1>


---

<h4 align="center"> Project created with focus on help to find the best place to live without have to do a bunch of clicks. </h4>

<br>

[![codecov](https://codecov.io/gh/rafaelandrade/wmh-scraper/branch/master/graph/badge.svg?token=0Q7YEZ5695)](https://codecov.io/gh/rafaelandrade/wmh-scraper)
![interrogate](interrogate_badge.svg)
[![DeepSource](https://deepsource.io/gh/rafaelandrade/wmh-scraper.svg/?label=active+issues&show_trend=true&token=UJMtOl1bqm06d0OL2Q_VbxJ4)](https://deepsource.io/gh/rafaelandrade/wmh-scraper/?ref=repository-badge)
<p>⭐ Star us on GitHub — it motivates us a lot!</p>

----

<h2> 👉 Quick start </h2>

This is a Python project focus on get public data from internet, using scraper as a main technologies implemented.

---
<h2> 🔌 Technologies </h2>

- Docker
- [AWS SQS](https://docs.aws.amazon.com/sqs/)
- [Sentry](https://docs.sentry.io/)
- [Coralogix](https://coralogix.com/integrations/coralogix-python-integration/)

---
<h2> ⚡️ First steps </h2>

The project WMH-Scraper is a Python program, and for the logic needs the [selenium](https://selenium-python.readthedocs.io/) 
library, and a navigator driver in these case is used [Google Chrome WebDriver](https://chromedriver.chromium.org/downloads). 

For the installation, the easiest mode is using the [docker](https://docs.docker.com/install/) technologies. Just follow the steps:

```bash
# Clone this repository
$ git clone https://github.com/rafaelandrade/wmh-scraper

# Access the project folder in the terminal/cmd
$ cd wmh-scraper

# Remember to clone the .env.example file to an .env file and fill the file.

# Starting building the docker container
$ docker-compose up

# To turn down the docker container
$ docker-compose down

```
----

## 🧚 Executing Tests

To execute the test is simple, have to options:

- Run `pytest` on terminal. Only remember to be in the root of the project.
- Or execute the follow code on terminal:

```shell 
./scripts/run_tests.sh
```

---

<h2> 🍕 Project assistance - Buy me a coffe </h2>

If you want to say thank you or/and support active development of WMH.

- Add a GitHub 🌟 to the project.
- Tweet and comment about project.
- Give was a coffee, if you like too.

<a href="https://www.buymeacoffee.com/rafaelasndrade" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A pizza" style="height: auto !important;width: auto !important;" ></a>

---
<h2> Contributing </h2>

Would you like to contribute to this project? [CONTRIBUTING.md](CONTRIBUTING.md) has all the details on how to do that.

---
<h2> ⚠️ License </h2>

WMH-Scraper is licensed under the terms of the GPL Open Source license and is available for free.