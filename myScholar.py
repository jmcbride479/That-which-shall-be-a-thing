import scholar


max_results=100
author='Daan Frenkel'


querier = scholar.ScholarQuerier()
settings = scholar.ScholarSettings()
settings.set_citation_format(scholar.ScholarSettings.CITFORM_REFWORKS)
querier.apply_settings(settings)
query = scholar.SearchScholarQuery()
query.set_author(author)

#max_results = min(max_results, scholar.ScholarConf.MAX_PAGE_RESULTS)
print 'Maximum nbr of results', max_results
query.set_num_page_results(max_results)


querier.send_query(query)
articles=querier.articles
print type(articles)
nArticles=len(articles)
print 'We found', nArticles,'for you querry'

if nArticles>0:
    for art in articles:
        attributes=art.attrs
        try:
            #print str(attributes['title'][0])
            print attributes['title'][0]
        except:
            print 'Cannot print title as str'
            try:
                print type(attributes['title'][0])
                print unicode(attributes['title'][0])
            except:
                print 'Cannot even print the type of title'
else:
    print "We did not find anything"
"""
for article in articles:
    print type(article)
"""

print attributes.keys()

print "Done"
