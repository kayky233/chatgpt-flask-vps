# chatgpt web server

1. 租用服务器

2. 登录并设置用户

   重设密码：

   ```
   passwd
   ```

   添加用户

   ```
   adduser kayky
   ```

   授予用户权限。

   ```
   usermod -aG sudo kayky
   ```

   切换到该用户

   ```
   su user_name
   ```

   

3. ###### 安装虚拟环境，假定已安装好python

   安装虚拟环境管理库virtualenv

   ```
   sudo pip3 install virtualenv
   ```

   查看库版本

   ```
   virtualenv --version
   ```

   创建虚拟环境，本项目基于Ubuntu 20.04，故python内置版本为3.8

   ```
   virtualenv --python=/usr/bin/python3.8 webapp
   ```

   切换至虚拟环境

   ```
   cd webapp
   ```

   激活虚拟环境

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
   pip3 install revChatGPT
   
   ```

   将openai key 添加到.env文件

   ```
   touch .env
   ```

   添加key将your_api_key替换为你的api key

   ```
   OPENAI_API_KEY=your_api_key
   ```

   

4. clone 代码

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

6. 创建flaskapp服务

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

   启动并查看状态

   ```
   sudo systemctl restart flaskapp
   sudo systemctl enable flaskapp
   sudo systemctl status flaskapp
   ```

   status 显示active且未报错则服务运行正常

7. 设置nginx

   安装nginx

   ```
   sudo apt-get install nginx
   ```

   设置nginx

   ```
   sudo vi /etc/nginx/sites-available/flaskapp
   ```

   添加如下内容：your_ip 需要替换为服务器ip，http://unix:/home/kayky/webapp/flaskapp.sock为.sock文件路径，需替换；kayky.tk 为domain name，需替换。

   ```
   server {
       listen 80;
       server_name your_ip;
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

   查看nginx log（如有必要）

   ```
   /var/log/nginx/error.log
   ```

   链接文件,贴个参考链接不细讲了：

   > https://medium.com/geekculture/deploying-flask-application-on-vps-linux-server-using-nginx-a1c4f8ff0010
   >

   ```
   sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled
   ```

   启动或重启nginx

   ```
   sudo systemctl restart nginx
   ```

   设置防火墙

   ```
   sudo ufw allow 'Nginx Full'
   ```
   
