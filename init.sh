sudo ln -s $(pwd)/config/nginx.conf /etc/nginx/conf.d/test.conf
sudo service nginx restart
gunicorn -b 127.0.0.1:8080 app.hello
