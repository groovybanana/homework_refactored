pages = [ {
    "filename": "./content/index.html", 
    "output": "./docs/index.html", 
    "title": "Home",
},
{
    "filename": "./content/blog.html", 
    "output": "./docs/blog.html", 
    "title": "Blog",
},
{
    "filename": "./content/about.html", 
    "output": "./docs/about.html", 
    "title": "About Me",
},
{
    "filename": "./content/contact.html", 
    "output": "./docs/contact.html", 
    "title": "Contact Me",
},
{
    "filename": "./content/portfolio.html", 
    "output": "./docs/portfolio.html", 
    "title": "Portfolio",
},
]



def main():

    print('rebuilding pages')
    top = open('./templates/top.html').read()
    bottom = open('./templates/bottom.html').read()

    for page in pages:
        filename = page['filename']
        output = page['output']
        title = page['title']
        page_content = page['filename'] 
        contents = open(page_content).read()
        open(output, 'w+').write(top + contents + bottom)
    print('rebuild complete')
main()

