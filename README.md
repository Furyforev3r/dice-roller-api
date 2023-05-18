> # :game_die: Dice-roller-API
+ **A dice rolling API done in python using fastAPI operating on https://dice-roller-api-production.up.railway.app/**
> ## :grey_question: How does it work?
+ **The API operates on the "REST API" model, returning a JSON as an HTTP GET response.**
> ## :desktop_computer: How to use?
+ **From GET requests with the parameter of the dice rolling operation, you will receive a JSON with the information generated from the parameter.**
+ **Example:** 
```python
requests.get("https://dice-roller-api-production.up.railway.app/1d20+15")
```
### **What can I put in the main parameter?**
+ **Common dice operations (Example: 1d20) and sum modifiers in operations (Example: 1d20+15).**
+ **It is also possible to roll several separate dice at once (Example: 1d20+10d6+15+15+1d100).**
