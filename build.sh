export PATH=$PATH:/opt/buildhome/.local/bin
git clone https://github.com/getpelican/pelican-themes.git /opt/buildhome/pelican-themes
echo ls -A $HOME
echo ls -A $HOME/pelican-themes
pip install markdown
pip install pelican
pelican content
