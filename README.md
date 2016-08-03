= misc-cache-attacks

- start the webserver

```axhttpd -p 127.0.0.1:8081 -s 127.0.0.1:8443 -key axtls-root/ssl/server.key -cert axtls-root/ssl/server.crt -w axtls-root/www```

- start the attack

```./client 127.0.0.1 8443```

- display resuts

```python results_to_js.py > display-results/js/data.js```

and open `display-results/index.html` in a browser
