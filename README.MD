# VETADMIN BACKEND

## Starter Open Source Project

- start config `uwsgi`

```
uwsgi --http :8080 --home <path-enviroment>/env --chdir <path-project>/backend/ -w conf.wsgi
```

- symlink
```
sudo ln -s /Users/claudiorojasrodriguez/src/personal/vetadmin/backend/vetadmin.conf /usr/local/etc/nginx/nginx.conf
```
