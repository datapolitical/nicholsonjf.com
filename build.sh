export PATH=$PATH:/opt/buildhome/.local/bin
git clone https://github.com/getpelican/pelican-themes.git /opt/buildhome
pip install pelican
pelican content
