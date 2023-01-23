# quetzpy :snake: :bird: :eyeglasses:
*Understand how people are talking of a topic based on a simple query*  

![](./media./../media/DALL·E%202022-11-15%2017.37.24%20-%20The%20body%20of%20a%20neon%20Quetzalcoatl%20,%20digital%20art.png)

- [quetzpy :snake: :bird: :eyeglasses:](#quetzpy-snake-bird-eyeglasses)
  - [1. WHAT IS IT?](#1-what-is-it)
  - [2. WHAT'S INSIDE THIS REPO ?](#2-whats-inside-this-repo-)
    - [2.1 root folder](#21-root-folder)
    - [2.2 src/quetzpy folder](#22-srcquetzpy-folder)
    - [2.3 \_\_config\_\_ folder](#23-__config__-folder)
    - [2.4 media folder](#24-media-folder)
  - [3. HOW TO USE IT ?](#3-how-to-use-it-)
  - [4. ABOUT THE PROJECT](#4-about-the-project)
  - [5. CONTACT THE AUTHOR](#5-contact-the-author)
  - [6. CONTRIBUTE](#6-contribute)

## 1. WHAT IS IT? 
The Queztzalcoatl project is the ability to **:eyes: excavate the :bird: Twitter API to extract insights about any topic that people talk about**.  
From a topic, you should be able to understand how people react using the power of text mining.

:arrow_up: *[Go to top page](#quetzpy-snake-bird-eyeglasses)*

## 2. WHAT'S INSIDE THIS REPO ?
```
Quetzalcoatl
├── /__config__
│   ├── DEMO_configuration_extractor.json
│   └── DEMO_configuration_runner.json
├── /media
├── /src/quetzpy
│       ├── /modules
│       │   ├── data_cleaning.py  
│       │   ├── data_mining.py  
│       │   ├── data_stats.py  
│       │   ├── decorators.py  
│       │   └── tweeter_connection.py  
│       ├── __init__.py
│       ├── extractor.py
│       ├── params_manager.py
│       └── runner.py
├── requirements.txt
├── demo.py
├── pyproject.toml
├── .gitignore  
├── README.md
└── LICENCE
```
### 2.1 root folder
You will find:
| File | Description |  
| ----------- | ----------- |  
| requirements.txt | Used by pip to install dependancies |  
| demo.py | The demo, [more information here]()  |   
| pyproject.toml | the configuration file to used for build library  |   
| .gitignore | - |   
| README.md | - |   
| LICENCE | - |   

### 2.2 src/quetzpy folder
You will find:
| File | Description |  
| ----------- | ----------- |  
| /src/quetzpy/\__init__.py | Package initializer |   
| /src/quetzpy/extractor.py | Class used to extract data from Twitter |   
| /src/quetzpy/params_manager.py | Class used to contain all the data needed to run the extractor and the runner |   
| /src/quetzpy/runner.py | Class used to run the extraction during a defined time and frequence |   


| File | Description |  
| ----------- | ----------- |  
| /src/quetzpy/modules | Contains modules used by the project |  
| /src/quetzpy/modules/data_cleaning.py | Module used to clean the tweets  |   
| /src/quetzpy/modules/data_mining.py | module used to extract insights from each tweets |   
| /src/quetzpy/modules/data_stats.py | module used to run some statistics from the mined data or tracked words |   
| /src/quetzpy/modules/decorators.py | module that contains all the decorators |   
| /src/quetzpy/modules/tweeter_connection.py | module used to connect to the Twitter API |   


### 2.3 \_\_config__ folder
You will find the two configuration files used by the demo script

### 2.4 media folder
Visuals and stuff


:arrow_up: *[Go to top page](#quetzpy-snake-bird-eyeglasses)*

## 3. HOW TO USE IT ?
Want to try the project? Please, follow the instructions from the Wiki page!



:arrow_up: *[Go to top page](#quetzpy-snake-bird-eyeglasses)*

## 4. ABOUT THE PROJECT
> I started this project a long time ago as my very first Python project. At first, I used some webscraping with Selenium as I didn't know how to use an API. As my experience with Python grew, I switched to the Twitter REST API and bash scripting and started think automation. Now, I am willing to create a package, or even an API inside which it would be possible to track an information inside a topic.

:arrow_up: *[Go to top page](#quetzpy-snake-bird-eyeglasses)*

## 5. CONTACT THE AUTHOR
> You can reach me on Twitter {[LINK](https://twitter.com/BeguinKyllian)}  
> I am also on LinkedIn {[LINK](https://www.linkedin.com/in/kyllian-b%C3%A9guin-733bbb150/)}

## 6. CONTRIBUTE
The Quetzalcoatl is a open source project. As so, if you feel interested in building the project with me, it would be amazing!  
Feel free to contact me on Twitter so I can tell you how you can help.  
We also have an issue page, [link here](https://github.com/KyllianBeguin/Quetzalcoatl/issues)!

:arrow_up: *[Go to top page](#quetzpy-snake-bird-eyeglasses)*