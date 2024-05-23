import wikipediaapi

# need to replace this with a proper way to randomly select months and dates
POD_Page = 'Chromodoris'

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
POD_py = wiki_wiki.page(POD_Page)

pageCounter = 0
birdCounter = 0
# print("Page - Title: %s" % page_py.title)

# Find random picture from Picture of the Day archives

def article_links(page):
    links = page.links
    links_To_Follow = []
    for title in sorted(links.keys()):
        # Remove all extraneous links. The title of the link can also function as a page title.
        # Need to find a way to only return articles that correspond to the POD
        # This list is returned alphabetical
        if not (title.__contains__('File:') or title.__contains__('Template') or title.__contains__('User:') or title.__contains__('Wikipedia:')):
            print(title, '............', type(title))
            links_To_Follow.append(title)

def link_To_Page(page):
    photoTitle = page.title
    articleTitle = photoTitle.replace('File:', "")
    toReplace = ['File:', '.svg', '.jpeg', '.png', '.gif', '.tiff', '.jpg']
    for i in toReplace:
        photoTitle = photoTitle.replace(toReplace[i], "")
    print('TITLE OF ACTUAL ARTICLE:', photoTitle)
    newPage = wiki_wiki.page(photoTitle)

    if newPage.exists():
        return newPage
    else:
        return None

# Return if current page is a part of a 'bird'-related category
def isBirdPage(page):
    categories = page.categories
    for title in sorted(categories.keys()):
        print(title, ".......", type(title))
        isBird = title.__contains__('bird') or title.__contains__('Bird')
        if isBird:
            return True
    return False

print('LINKS')
article_links(POD_py)

print("CATEGORIES")
if isBirdPage(POD_py):
    birdCounter += 1
