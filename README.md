# Quetzalcoatl :snake: :bird: :eyeglasses:
*Understand how people are talking of your shows based on your query*

## SUMMARY
1. [WHAT IS IT?](#whatisit)
2. [WHAT'S INSIDE THIS REPO ?](#whatinsiiderepo)
3. [HOW TO USE IT ?](#howtouseit)
4. [ABOUT THE PROJECT](#abouttheproject)
5. [CONTACT THE AUTHOR](#contactauthor)

## <a name="whatisit"></a> 1. WHAT IS IT? 
The Queztzalcoatl project is the ability to **excavate the Twitter API to extract insights about any topic that people talk about**.  
From a topic, you should be able to understand how people react using the power of text mining.

## <a name="whatinsiiderepo"></a> 2. WHAT'S INSIDE THIS REPO ?
```
├── modules  
│   ├── data_cleaning.py  
│   ├── data_mining.py  
│   └── tweeter_connection.py  
├── bearer_token.json  
├── demo.py  
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


## <a name="howtouseit"></a> 3. HOW TO USE IT ?
There is a really cool demo here {[LINK](demo.py)}  

1. As the Quetzalcoatl is going to query Twitter's API, you need to put your **bearer token** in the bearer_token.json file {[LINK](bearer_token.json)}  

2. Once you done it, go to the demo.py and **change the topic**:
``` python
Quetzal = Quetzalcoatl.Quetzalcoatl(bearer_token, topic = "#MarcheContreLaVieChere")
```
3. Almost there, just need to **give a language** if you wish to:
``` python
Quetzal.extract_tweets(lang='')
```
4. And **run demo.py** !  
``` bash
python ./demo.py
```

## <a name="abouttheproject"></a> 4. ABOUT THE PROJECT
> I started this project a long time ago as my very first Python project. At first, I used some webscraping with Selenium as I didn't know how to use an API. As my experience with Python grew, I switched to the Tweeter REST API and bash scripting and started think automation. Now, I am willing to create a package, or even an API in which it would be possible to track an information inside a topic.

## <a name="contactauthor"></a> 5. CONTACT THE AUTHOR
> You can reach me on Twitter {[LINK](https://twitter.com/BeguinKyllian)}  
> I am also on LinkedIn {[LINK](https://www.linkedin.com/in/kyllian-b%C3%A9guin-733bbb150/)}