import requests

exeptions = [   'https://fonts.googleapis.com',
                'https://fonts.gstatic.com',
                '/SEVER/styles/landing.css',
                'https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap',
                'https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;500;700&display=swap',
                'https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.min.css'
                 ]



current_page = requests.get('https://dicantnik.github.io/SEVER/pages/landing.html')
print(current_page.text)
split = current_page.text.split('href="')
links = []
for text in split:
    link = text.split('"')[0]
    if link not in exeptions:
            links.append(link)
links.pop(0)

print(links)


