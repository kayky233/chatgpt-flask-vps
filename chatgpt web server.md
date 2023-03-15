# chatgpt web server

1. 租用服务器

2. 登录并设置用户

   ```
   重设密码：passwd
   ```

   

   ```
   adduser kayky
   ```

   ```
   usermod -aG sudo kayky
   ```

   ```
   su user_name
   ```

   

3. ###### 安装虚拟环境

   ```
   sudo pip3 install virtualenv
   ```

   ```
   virtualenv --version
   ```

   创建虚拟环境，20.04为3.8

   ```
   virtualenv --python=/usr/bin/python3.8 webapp
   ```

   ```
   cd webapp
   ```

   ```
   source bin/activate
   ```

   安装所需库

   

   ```
   pip3 install wheel
   pip3 install flask
   pip3 install gunicorn
   pip3 install openai
   pip3 install python-dotenv
   
   ```

   

4. get 代码

   ```
   git clone https://github.com/kayky233/chatgpt-flask-vps.git
   ```

   拷贝到webapp文件夹下

   ```
   cp -r ./chatgpt-flask-vps/* ./
   ```

5. 测试网页是否有问题

   ```
   sudo ufw allow 5000
   ```

   ```
   python3 flaskapp.py
   ```

   

6. 创建app服务

   ```
   sudo vi /etc/systemd/system/flaskapp.service
   ```

   ```
   [Unit]
   Description=A Gunicorn example to serve Flask project
   After=network.target
   [Service]
   User=kayky
   Group=www-data
   WorkingDirectory=/home/kayky/webapp/
   Environment="PATH=/home/kayky/webapp/bin"
   ExecStart=/home/kayky/webapp/bin/gunicorn --workers 3 --bind unix:/home/kayky/webapp/flaskapp.sock -m 007 wsgi:app
   [Install]
   WantedBy=multi-user.target
   Description=A Gunicorn example to serve Flask project
   After=network.target
   ```

   ```
   sudo systemctl restart flaskapp
   sudo systemctl enable flaskapp
   sudo systemctl status flaskapp
   ```

   

7. nginx

   ```
   sudo apt-get install nginx
   ```

   ```
   sudo vi /etc/nginx/sites-available/flaskapp
   ```

   设置超时时间

   ```
   server {
       listen 80;
       server_name 45.76.204.142;
       proxy_read_timeout 300s;
   location / {
                include proxy_params;
                proxy_pass http://unix:/home/kayky/webapp/flaskapp.sock;
                proxy_read_timeout 300;
       }
   }
   server {
       listen 80;
       server_name kayky.tk www.kayky.tk;
       proxy_read_timeout 300s;
   
       location / {
           include proxy_params;
           proxy_pass http://unix:/home/kayky/webapp/flaskapp.sock;
           proxy_read_timeout 300;
       }
   }
   ```

   查看nginx log

   ```
   /var/log/nginx/error.log
   ```

   

   ```
   sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled
   ```

   ```
   sudo systemctl restart nginx
   ```

   ```
   sudo ufw allow 'Nginx Full'
   ```

   