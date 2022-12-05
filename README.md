# Quetzalcoatl :snake: :bird: :eyeglasses:
*Understand how people are talking of a topic based on a simple query*
![](./media./../media/DALL·E%202022-11-15%2017.37.24%20-%20The%20body%20of%20a%20neon%20Quetzalcoatl%20,%20digital%20art.png)

## SUMMARY
- [Quetzalcoatl :snake: :bird: :eyeglasses:](#quetzalcoatl-snake-bird-eyeglasses)
  - [SUMMARY](#summary)
  - [1. WHAT IS IT?](#1-what-is-it)
  - [2. WHAT'S INSIDE THIS REPO ?](#2-whats-inside-this-repo-)
  - [3. HOW TO USE IT ?](#3-how-to-use-it-)
  - [4. ABOUT THE PROJECT](#4-about-the-project)
  - [5. CONTACT THE AUTHOR](#5-contact-the-author)
  - [6. CONTRIBUTE](#6-contribute)

## 1. WHAT IS IT? 
The Queztzalcoatl project is the ability to **excavate the Twitter API to extract insights about any topic that people talk about**.  
From a topic, you should be able to understand how people react using the power of text mining.

*[Go to top page](#summary)*

## 2. WHAT'S INSIDE THIS REPO ?
```
Quetzalcoatl
├── modules  
│   ├── data_cleaning.py  
│   ├── data_mining.py  
│   └── tweeter_connection.py  
├── bearer_token.json  
├── main_setup.json  
├── main.py  
├── Quetzalcoatl.py  
├── .gitignore  
├── README.md  
└── TO_DO.md  
```


You will find:
| File | Description |  
| ----------- | ----------- |  
| modules | Contains the modules for tweeter mining, data cleaning and data mining |  
| bearer_token.json | To store your token |   
| demo.py | to run the demo  |   
| Quetzalcoatl.py | Main class |   
| TO_DO.md | To keep track of all the stuff I did on the project |   

*[Go to top page](#summary)*

## 3. HOW TO USE IT ?
There is a really cool demo here {[LINK](demo.py)}  

:one: First, ss the Quetzalcoatl is going to query Twitter's API, you need to put your **bearer token** in the [bearer_token.json](bearer_token.json) file

:two: Once you done it, go to the main_setup.json to setup main script like this:
``` json
{
    "words to catch" : ["sécurité", "Mont saint michel"],
    "topics" : ["Normandie", "Bretagne"],
    "numbers of runs" : 20,
    "sleeping time" : [60,5],
    "lang" : "fr"
}
```

Here is a table that describe each parameter:
| parameter   | Description |
| -------- | ----------- |
| `words to catch` | List of words that you want to count in the bunch of tweets |
| `topics` | List of topics that you want to query, can be hashtags or else |
| `numbers of runs` | The number of times you want to run the script |
| `sleeping time` | The time, in seconds, to wait for the script before runing again. |
| `lang` | Language |

:three: And **run main.py** !  
``` bash
python ./main.py
```

*[Go to top page](#summary)*

## 4. ABOUT THE PROJECT
> I started this project a long time ago as my very first Python project. At first, I used some webscraping with Selenium as I didn't know how to use an API. As my experience with Python grew, I switched to the Twitter REST API and bash scripting and started think automation. Now, I am willing to create a package, or even an API inside which it would be possible to track an information inside a topic.

*[Go to top page](#summary)*

## 5. CONTACT THE AUTHOR
> You can reach me on Twitter {[LINK](https://twitter.com/BeguinKyllian)}  
> I am also on LinkedIn {[LINK](https://www.linkedin.com/in/kyllian-b%C3%A9guin-733bbb150/)}

## 6. CONTRIBUTE
The Quetzalcoatl is a open source project. As so, if you feel intrested in helping the tool with me, it would be amazing!  
To help you, two documents exists. The first one, the [TO DO list](./TO_DO.md), is a list of  every feature to implement. The second one, the [Isses table](./Issues.md), is a table of every issues raised and documented.