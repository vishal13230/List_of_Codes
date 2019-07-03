import wikipedia
print(wikipedia.search("arpit", results = 2))
print(wikipedia.suggest("vishal raj"))
print(wikipedia.summary("plastic"))
print(wikipedia.summary("python", sentences = 2))
wikipedia.page("python")
wikipedia.page("python").content

print(wikipedia.page("Python").url) 
print(wikipedia.page("Python").references)