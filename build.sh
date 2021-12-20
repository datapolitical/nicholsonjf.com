export PATH=$PATH:/opt/buildhome/.local/bin
git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes
ls -l $HOME
ls -l $HOME/pelican-themes/pelican-bootstrap3
pip install markdown
pip install pelican
pelican content
