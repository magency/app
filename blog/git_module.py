#!/usr/bin/python
import git
import os
from git import *

class GitClass:

	#Variables
	def __init__(self):
		self.clone=""
		self.repo=""
		self.branch=""
		self.remotes=""
		self.target="repoDir"
		self.source="git@git.magency.fr:nassim/rapport-de-stage.git"
		self.deb="debian"
		self.ver="0.0.1"

	#Methods 
	def git_clone(self, source, target, deb, ver):
		try:
	   		with open(target): pass
			with open(deb+"_"+ver+"_all.deb"): pass
		except IOError:
	   		print 'Folder to use for cloning already exists.'
	   		print 'Debian package already exists.'
	   		print 'Removing in progress...'
	      	os.system("rm -rf "+target)
	      	os.system("rm -rf "+deb+"_"+ver+"_all.deb")
	   	  	
	    #CLONING
		print '\nCloning from '+source+' to '+target
		print '\nIn progress...'
		clone= git.Repo.clone_from(source, target)
		
		#REMOTE BRANCHES
		self.branch= clone.git.branch(r=True)
		self.remotes=[remote.strip() for remote in self.branch.splitlines()]
		print '\nRemote branches'
		print self.remotes

		#MAKING DEB PACKAGE
		print '\nMaking Debian package'
		os.system("fpm -s dir -t deb -a all -n "+deb+" -v "+ver+" -C "+target+" .")

		#GIT STATUS & BRANCHES
		repo= git.Repo(target)
		print '\nGit status'
		print repo.git.status()
		print '\nList of branches'
		print repo.git.branch()
#TEST 
#git://gitorious.org/git-python/mainline.git
#git@git.magency.fr:nassim/rapport-de-stage.git	 	
instance= GitClass()
instance.git_clone(instance.source, instance.target, instance.deb, instance.ver)