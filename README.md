# hr-test-python

This is the interview questions for python dev skills.

---
### 1. How do you setup local python dev environment?  
- What IDE do you use?

**Mostly I’ve been using Anaconda Navigator:  Spyder, Jupyter notebook, PyCharm.**

- How do you setup python production environment in Linux?
  - List the cli commands if possible.

**I personally use conda, I create my virtual project specific env on conda. However, I give general approach for setup on Linux.**

**
a) Open a Linux terminal.
b) Choose the directory, where you want to create new environment.
c) Make sure that your system updated to latest versions:  sudo apt update
d) Check python installed or not?  python --version
e) If not installed, then install right version of python. 
f)                    sudo apt-get install python#
g) Make sure pip installed:  sudo apt install python3-pip python3-dev
h) Install virtualenv  pip3 install virtualenv
i) Create new env ‘houseprice_pred_env’   
j)                 python3 –m venv houseprice_pred_env or virtualenv venv houseprice_pred_env
k) Activate new env   source houseprice_pred_env /bin/activate
l) Install ML Libraries:  pip install numpy pandas scikit-learn tensorflow etc..
m) suppose we have above env already in local then run command.  pip freeze > requirements.txt
n) n production, we can install same with one command.  pip install -r requirements.txt
**
---
### 2. Are you familiar using any linux distro?
**Yes**
- crontab
**I am big fan of crontab, I have used to schedule jobs and run python script or ML models in necessary environment. We can schedule jobs on required frequency basis…like daily, hourly, weekly, every monthly etc. 
	Eg: ‘crontab -l’: This will give the list of currently scheduled tasks**

**Below three are familiar to me but didn’t get much chance to exploit it**

- ssh 
- nfs
- nginx

---
### 3. Setup a RESTful API with python & nginx.
- Using localhost
- Free to choose any python web component
- All outputs in JSON

API definition: /timestamp
> return current UNIX timestamp
```
# Test command:
curl 127.0.0.1/timestamp

# Expected outcome:
{"timestamp":1624900201}
```

API definition: /readdata
> read POST JSON input and send it back
```
# Test command:
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"abc","password":"xyz"}' \
  http://127.0.0.1/readdata

# Expected outcome:
{"username":"abc","password":"xyz"}
```

bad input
```
# Test command:
curl 127.0.0.1/noexist

# Expected outcome:  (404)
... 
404 Not Found 
...
```

#### What to submit:
- Python code **Provided python code via my github link**

---
### 3.1 Nginx (Optional)
- Use Nginx as the front web server (reverse proxy)
- deploy python program on port 8000

#### What to submit:
- Nginx server config
