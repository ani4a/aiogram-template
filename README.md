
# Aiogram-Template

Template for creating new telegram bots


## Download and run

Download project

```bash
git clone https://github.com/ani4a/aiogram-template.git
```


Install dependencies

```bash
cd aiogram-template
pip3 install -r requirements.txt
```

Setup config

[API KEY](https://t.me/botfather)

```bash
cp config.ini.example config.ini
nano config.ini
```

Run with systemd

```bash
sudo cat >/etc/systemd/system/aiogram-template.service <<EOL
Description=Aiogram Template
After=multi-user.target

[Service]
Type=simple
Restart=always
WorkingDirectory=/yourdir
ExecStart=python3 -m app

[Install]
WantedBy=multi-user.target

EOL
```
```bash
sudo systemctl enable --now aiogram-template.service

```
## License

[MIT](https://choosealicense.com/licenses/mit/)

