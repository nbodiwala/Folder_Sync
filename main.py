from subprocess import call

source = '//femoran.com/fem/company/1-Open Projects/109967000 - 218 E Grand/Engineering and BIM/07_FEM Shop/01_Current PDF'
destination = 'C:/Users/nbodiwala/Dropbox (Moran Group)/109967000 - 218 E Grand-Current PDFs'

call(['robocopy', source, destination, '*.pdf', '/S', '/XD', '*_archive'])