### ENV
```bash
python3 -m venv venv --upgrade-deps
. venv/bin/activate
```
### DEPS
```bash
pip install -r ./requirements.txt 
```
### DB
```
psql -U postgres
CREATE DATABASE ioc;
```
### PLAY
```bash
flask db --help             # migration
flask run --debug
```
### DUMMY
```
psql -U postgres -d ioc
INSERT INTO user (id, name) VALUES (1, Phil)
INSERT INTO user (id, name) VALUES (2, Dom)
\quit
```
### CHECK
```
http://localhost:5000/user/1
http://localhost:5000/user/2
```
### FORMATTER
```bash
yapf -i [file].py
```
