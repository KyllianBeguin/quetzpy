# TO DO  
- [ ] Deal with hashtags with complexe construction  
    - [ ] With an underscore  
- [ ] Get some stats  
  - [ ] Occurence of hashtags  
  - [ ] Dependency of other hashtags  


# DONE  
- [X] Do the 'hashtags extraction' function  
  - [X] Check the "unhashable type" issue (#PB01)  
      -> Issue was the curly brackets around the parameter in the print function (example : print({value}))  
- [X] Make the 'mentions extraction' function  
- [X] Deal with hashtags with complexe construction  
    - [X] With a dash, example : #day-one  
        -> Dashed hashtags doesn't work. In Twitter, such hashtags are not taken as full hastags. Only #day will be use as hashtag in #day-one  
- [X] Make the 'link cleansing' function  
 