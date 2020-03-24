print('hello world')

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
