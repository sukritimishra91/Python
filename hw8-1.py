from queue import LifoQueue
import re

def checkBalancedHtmlTags(file):
    if file is None or len(file) == 0:
        print('Enter an html file')
        return
    # more html tags can be added in the lists but I have taken these much for simplicity
    openTags = ['<html>', '<head>', '<body>', '<title>', '<p>', '<a>', '<h1>']
    closeTags = ['</html>', '</head>', '</body>', '</title>', '</p>', '</a>', '</h1>']
    stack = LifoQueue()
    with open(file) as f:
        for line in f:
            tagsFound = re.findall('<[/]?[a-z|0-9]*>', line.lower())
            for tag in tagsFound:
                if tag in openTags:
                    stack.put(tag)
                elif tag in closeTags:
                    poppedTag = stack.get()
                    if tag.replace('/','') != poppedTag:
                        return False
    return stack.empty()

isHtmlBalanced = checkBalancedHtmlTags('test.html')
if isHtmlBalanced:
    print('Html tags balanced')
else:
    print('Html tags not balanced')