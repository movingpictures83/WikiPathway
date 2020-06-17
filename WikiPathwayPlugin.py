import sys
import pypathway
from pypathway import PublicDatabase

class WikiPathwayPlugin:
   def input(self, inputfile):
      self.query = inputfile[inputfile.rfind('/')+1:]

   def run(self):
      self.results = PublicDatabase.search_wp(self.query)

   def output(self, outputfile):
      outfile = open(outputfile, 'w')
      for reaction in set(self.results):
         outfile.write("***************************************\n")
         outfile.write(str(reaction))
         outfile.write("***************************************\n")
