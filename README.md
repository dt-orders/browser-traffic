# Overview

This is a simple script to send some browser traffic to the dt-orders app with a configurable loop count and base URL.  

See the [overview repo](https://github.com/dt-orders/overview) for how to setup the application.

# Running

Assuming the dt-orders app is running, start docker with this command and adjust arguments as needed.

```
docker run -it \
    --env SCRIPT_NUM_LOOPS=1 \
    --env APP_URL=http://172.17.0.1 \
    dtdemos/dt-orders-broswer:1
```

Use `start-browser.sh` and `stop-browser.sh` as a helper script to test the docker image.

```
# example override of URL to run for 10000 loops, in detached more
sudo ./start-browser.sh http://44.234.152.110 10000

# example override of URL to run for 5 loops, in foreground DEBUG mode
sudo ./start-browser.sh http://44.234.152.110 5 true
```

# Development

## Prerequisites - This is setup on a mac

```
# Install Python 3.x
brew install python
python --version

# Install Pip
pip install pip
pip install --user pipenv

# Install required packaged
pip install -r requirements.txt
```

## Install Chromedriver.  
See versions [here](http://chromedriver.storage.googleapis.com/)

```
curl chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_mac64.zip -o chromedriver_mac64.zip
unzip chromedriver_mac64.zip chromedriver -d /usr/local/bin/
rm chromedriver_mac64.zip
chromedriver --version
```

## Develop and Test

* Edit script and run it  

    ```
    # with no browser showing
    python app.py --url http://localhost --num_loops 1

    # with browser showing
    python app.py --show --url http://localhost --num_loops 1
    ```
    
* Use `buildpush.sh` to build and push the Docker image
