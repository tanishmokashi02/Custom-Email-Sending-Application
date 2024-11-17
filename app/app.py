#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():
    return {"message": "Welcome to the Email Sender app!"}


# In[ ]:


from bottle import route, run, template

@route('/')
def home():
    return template('<b>Hello, World!</b>')

run(host='localhost', port=8080)


# In[ ]:


get_ipython().system(' pip install bottle')


# In[ ]:




