def main():

    print('rebuilding pages')

    top = open('./templates/top.html').read()
    bottom = open('./templates/bottom.html').read()

    index = open('./content/index.html').read()
    blog = open('./content/blog.html').read()
    about = open('./content/about.html').read()
    contact = open('./content/contact.html').read()
    portfolio = open('./content/portfolio.html').read()



    open('./docs/index.html', 'w+').write(top + index + bottom)
    open('./docs/blog.html', 'w+').write(top + blog + bottom)
    open('./docs/about.html', 'w+').write(top + about + bottom)
    open('./docs/contact.html', 'w+').write(top + contact + bottom)
    open('./docs/portfolio.html', 'w+').write(top + portfolio + bottom)
    print('rebuilding complete')

main()

pages = [ {
    "filename": "content/index.html", 
    "output": "docs/index.html", 
    "title": "Home",
},
{
    "filename": "content/blog.html", 
    "output": "docs/blog.html", 
    "title": "Blog",
},
{
    "filename": "content/about.html", 
    "output": "docs/about.html", 
    "title": "About Me",
},
{
    "filename": "content/contact.html", 
    "output": "docs/contact.html", 
    "title": "Contact Me",
},
{
    "filename": "content/portfolio.html", 
    "output": "docs/portfolio.html", 
    "title": "Portfolio",
},
]

for page in pages:
    filename = page['filename']
    output = page['output']
    title = page['title']
    print('filename is:', filename)
    print('output name is:', output)
    print('ttle of page is:', title)

# for page in pages:
# print(page) # Replace this line


# Where "page" is a dictionary with a key "title"
# page_title = page[title] 
# print(page_title)