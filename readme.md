

# Environment

```python
python=3.9.0
kivy=2.3.0
kivymd=1.2.0
pandas=2.2.1
```

# Installation
```bash
# clone this repository
git clone https://github.com/yisnsiy/goal.git

# create direction named 'figure' in '/' dir for using of figures
mkdir figure

# copy data_example.csv into '/src/' dir
cp data_example.csv ./src/data.csv

```

# Building APP

```bash
# motify buildozer.spec for yourself
vim /src/buildozer.spec

# create android app
buildozer -v android debug

```