this is a simple website working with flask and docker to compute the nth fibonacci number

to run it, you simply have to run the following commands:
- sudo docker build -t my-flask-app .
- sudo docker run -d -p 5000:5000 my-flask-app
You now have a running website on the following address :
- 172.17.0.2:5000
- or on the localhost:5000

enjoy the website ! 

number 15