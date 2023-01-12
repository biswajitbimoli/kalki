import re


a = """

* {
padding: auto;
margin: 0em 4vh 2em 4vh;
border: 2px solid red;
}
.bg-red {
background-color: red;
}
.text-red {
color: red;
}
.bg-green {
background-color: green;
}
.text-green {
color: green;
}
.bg-blue {
background-color: blue;
}

"""



class MinifyLogic:
    def __init__(self, cssfile):
        self.cssfile = cssfile
    
    def minify_file(self):
        new = ''
        css = list(re.finditer(r':.+;', self.cssfile))
        new += re.sub(r'\s','',self.cssfile[:css[0].span()[0]])
        length = len(css)
        for i in range(length-1):
            new += css[i][0][0] + css[i][0][1:len(css[i][0])-1].strip() + css[i][0][len(css[i][0])-1] + re.sub(r'\s', '', self.cssfile[css[i].span()[1]:css[i+1].span()[0]])
        
        new += re.sub(r'\s', '', self.cssfile[css[length-1].span()[0]:])
        return new
