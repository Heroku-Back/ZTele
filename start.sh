curl -sL https://deb.nodesource.com/setup_20.x | bash - && apt-get install -y nodejs && apt-get -qq update && apt-get -qq install -y git wget ffmpeg mediainfo && pip install --upgrade pip && pip3 install -r requirements.txt
