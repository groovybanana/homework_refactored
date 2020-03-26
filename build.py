pages = [ {
    "filename": "./content/index.html", 
    "output": "./docs/index.html", 
    "title": "Chris Moe's Spring 2020 bootcamp project",
},
{
    "filename": "./content/blog.html", 
    "output": "./docs/blog.html", 
    "title": "My personal blog",
},
{
    "filename": "./content/about.html", 
    "output": "./docs/about.html", 
    "title": "Learn all about Me",
},
{
    "filename": "./content/contact.html", 
    "output": "./docs/contact.html", 
    "title": "Reach out and get in touch with me",
},
{
    "filename": "./content/portfolio.html", 
    "output": "./docs/portfolio.html", 
    "title": "A selection of stuff I have built",
},
]


def apply_template():
    template = open("./templates/base.html").read()
    return template

def combine(contents):
    template = apply_template()
    finished_combined_page = template.replace("{{content}}", contents)
    return finished_combined_page 

def main():
    print('rebuilding pages')
    for page in pages:
        filename = page['filename']
        output = page['output']
        title = page['title']
        contents = open(filename).read()
        open(output, "w+").write(combine(contents))
        print(output)
    print('rebuild complete')
main()
