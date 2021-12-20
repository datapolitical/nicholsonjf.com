export PATH=$PATH:/opt/buildhome/.local/bin
git clone https://github.com/getpelican/pelican-themes.git /opt/buildhome/pelican-themes
ls -l $HOME
ls -l $HOME/pelican-themes
pip install markdown
pip install pelican
pelican content
