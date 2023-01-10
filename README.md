# Quetzalcoatl :snake: :bird: :eyeglasses:
*Understand how people are talking of a topic based on a simple query*  

![](./media./../media/DALL·E%202022-11-15%2017.37.24%20-%20The%20body%20of%20a%20neon%20Quetzalcoatl%20,%20digital%20art.png)

- [Quetzalcoatl :snake: :bird: :eyeglasses:](#quetzalcoatl-snake-bird-eyeglasses)
  - [1. WHAT IS IT?](#1-what-is-it)
  - [2. WHAT'S INSIDE THIS REPO ?](#2-whats-inside-this-repo-)
    - [2.1 root folder](#21-root-folder)
    - [2.2 src folder](#22-src-folder)
    - [2.3 \_\_config\_\_ folder](#23-__config__-folder)
    - [2.4 media folder](#24-media-folder)
  - [3. HOW TO USE IT ?](#3-how-to-use-it-)
  - [4. ABOUT THE PROJECT](#4-about-the-project)
  - [5. CONTACT THE AUTHOR](#5-contact-the-author)
  - [6. CONTRIBUTE](#6-contribute)

## 1. WHAT IS IT? 
The Queztzalcoatl project is the ability to **:eyes: excavate the :bird: Twitter API to extract insights about any topic that people talk about**.  
From a topic, you should be able to understand how people react using the power of text mining.

:arrow_up: *[Go to top page](#summary)*

## 2. WHAT'S INSIDE THIS REPO ?
```
Quetzalcoatl
├── /__config__
│   ├── DEMO_configuration_extractor.json
│   └── DEMO_configuration_runner.json
├── /media
├── /src
│   ├── /modules
│   │   ├── data_cleaning.py  
│   │   ├── data_mining.py  
│   │   ├── data_stats.py  
│   │   ├── decorators.py  
│   │   └── tweeter_connection.py  
│   └── Quetzalcoatl.py
├── requirements.txt
├── demo.py
├── .gitignore  
├── README.md
└── LICENCE
```
### 2.1 root folder
You will find:
| File | Description |  
| ----------- | ----------- |  
| requirements.txt | Used by pip to install dependancies |  
| demo.py | A demo script  |   
| .gitignore | - |   
| README.md | - |   
| LICENCE | - |   

### 2.2 src folder
You will find:
| File | Description |  
| ----------- | ----------- |  
| /src/modules | Contains modules used by the project |  
| /src/modules/data_cleaning.py | module used to clean the tweets  |   
| /src/modules/data_mining.py | module used to extract insights from each tweets |   
| /src/modules/data_stats.py | module used to run some statistics from the mined data or tracked words |   
| /src/modules/decorators.py | module that contains all the decorators |   
| /src/modules/tweeter_connection.py | module used to connect to the Twitter API |   
| /src/Quetzalcoatl.py | Contains all the classes of the project |   

### 2.3 \_\_config__ folder
You will find the two configuration files used by the demo script

### 2.4 media folder
All the stuff that are used to produce documents


:arrow_up: *[Go to top page](#summary)*

## 3. HOW TO USE IT ?
Want to try the project? Please, follow the instructions from the Wiki page!



:arrow_up: *[Go to top page](#summary)*

## 4. ABOUT THE PROJECT
> I started this project a long time ago as my very first Python project. At first, I used some webscraping with Selenium as I didn't know how to use an API. As my experience with Python grew, I switched to the Twitter REST API and bash scripting and started think automation. Now, I am willing to create a package, or even an API inside which it would be possible to track an information inside a topic.

:arrow_up: *[Go to top page](#summary)*

## 5. CONTACT THE AUTHOR
> You can reach me on Twitter {[LINK](https://twitter.com/BeguinKyllian)}  
> I am also on LinkedIn {[LINK](https://www.linkedin.com/in/kyllian-b%C3%A9guin-733bbb150/)}

## 6. CONTRIBUTE
The Quetzalcoatl is a open source project. As so, if you feel interested in building the project with me, it would be amazing!  
Feel free to contact me on Twitter so I can tell you how you can help.  
We also have an issue page, [link here](https://github.com/KyllianBeguin/Quetzalcoatl/issues)!

:arrow_up: *[Go to top page](#summary)*