
# Kalki

Kalki is a CSS syntax enhancement tool build in python


## Here is the guide to working through it




## Installation

You can download latest version from the github or clone it.
    
## This is how Our file system Works







![Screenshot from 2023-01-01 21-56-00](https://user-images.githubusercontent.com/46971615/210178899-e5c66ffd-a470-40aa-8e62-da2d050cbb24.png)

Here you can see we have, kalki.kalki, service.py and kalkiminify.py files mainly.

## kalki.kalki

kalki.kalki is the main file where we will be writing our css code, or more precisely css code with enhanced features.

## service.py

This is the main file which compiles .kalki files to Browser readable .css file

## kalkiminify.py

This file minifies css code that is compiled from kalki.kalki

Till the time you will need to have exact kalki.kalki name of your .kalki file to compile it to css

## Syntax
### kalki.kalki follows following syntax rules
.kalki syntax is as same as .css syntax but with python code integration. You can write .css code in .kalki as well, it just extends more features with python code between two @kalki tag.

```python/css
* {
    padding: auto;
}
.container {
  width: 600px;
  height: 800px;
}
@kalki
for i in range(5):
  style = @css
  .mt-{i} ${
    margin-top: {i}em;
  }$
  @end
  @addkalki
@kalki
```
Here you can see in first two code, it is pure css and bellow that we have python code(with little bit of modification) between @kalki tags

#### @kalki
@kalki tag is very important for out compiler to understand that it is a .kalki enhanced css code and has to be compiled in order to make it browser readable. without this tag at the start and at the end, the code is supposed to be plain string by the compiler.

```python/css
@kalki
for i in range(5):
  style = @css
  .mt-{i} ${
    margin-top: {i}em;
  }$
  @end
  @addkalki
@kalki
```

inside python code you see we have css code assigned to style variable. This style variable is also very important and all the css code needs to be assigned to this variable. This variable will be added to the compiled .css file.

All the css codes are written between the @css and @end tag. It is neccessary parameters, compiler listens to these tags and decides that the code between these two tags are the main css codes.

{}, curly braces are used to insert dynamic values in the code.

And we have ${}$ which replaces traditional css curly braces
```python/css
* {
    padding: auto;
}
.container {
  width: 600px;
  height: 800px;
}
```
This is due to the {}, curly braces which we use to insert dynamic value, so we can not use this braces for other purpose.

And at last we have @addkalki tag, which is required to add at the last with proper indentation. this tag allows compiler to add the given dynamic .kalki code to compiled .css file.
