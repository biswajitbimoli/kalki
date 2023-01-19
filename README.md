
# Kalki

Kalki is a CSS syntax enhancement tool build in python


## Here is the guide to working through it




## Installation

You can download latest version from PyPy using pip

```bash
  pip install kalki
  kalki startproject <project_name>
  cd <project_name>
  python manage.py startapp <app_name>
```
    
## This is how Our file system Works

Your working app is available under 'styles' sub-direcotry within your main app. <app_name>.kalki is the file where all CSS code will be written on.

You can add more app to your project by-
```bash
  python manage.py startapp <other_app_name>
```
Make sure to add <other_app_name> in APP_NAME under settings.py of your root project.

## .kalki

.kalki is the extension kalki uses to write CSS dynamically.

## Syntax
### kalki.kalki follows following syntax rules
.kalki syntax is as same as .css syntax but with python code integration. You can write .css code in .kalki as well, it just extends more features with python code between two @kalki and @endkalki tag.

```python/css
@kalki_global

colors = ['red', 'green', 'blue', 'purple', 'orange', 'black']

@endkalki


* {
    padding: auto;
}

@kalki
for color in colors:
    @css
    .bg-{{color}} {
        background-color: {{color}};
    }
    @endcss
for color in colors:
    @css
    .text-{{color}} {
        color: {{color}};
    }
    @endcss
@endkalki
```
Here you can see in first two code, it is pure css and bellow that we have python code(with little bit of modification) between @kalki and @endkalki tags. We use @kalki_global and @endkalki to write global variable.

#### @kalki and @endkalki
@kalki tag is very important for out compiler to understand that it is a .kalki enhanced css code and has to be compiled in order to make it browser readable. without this tag at the start and at the end, the code is supposed to be plain string by the compiler.

```python/css
@kalki
for color in colors:
    @css
    .text-{{color}} {
        color: {{color}};
    }
    @endcss
@endkalki
```

inside python code you see we have css code assigned to style variable. This style variable is also very important and all the css code needs to be assigned to this variable. This variable will be added to the compiled .css file.

All the css codes are written between the @css and @endcss tag. It is neccessary parameters, compiler listens to these tags and decides that the code between these two tags are the main css codes.

{{}}, curly braces are used to insert dynamic values in the code.

