#!/bin/bash
#
# Accepted parameters:
#
# Version: Boundless Desktop's version (e.g. 1.0)

set -e

Version=$1
# Clean things up
mkdir -p tmp
cd tmp
rm -rf output 
mkdir output

# Getting QGIS Core Documentation

if [ ! -d "QGIS-Documentation" ]; then
  git clone https://github.com/qgis/QGIS-Documentation.git;
fi
cd QGIS-Documentation;

rm -rf output;

case "$Version" in
	"1.0")
		git fetch origin manual_en_2.14;
		git checkout manual_en_2.14;
		git merge origin/manual_en_2.14;
		;;
	*)
		git checkout master;
		git pull origin master;
		;;
esac

if [ -d "qgisdocs_virtualenv" ]; then
   source qgisdocs_virtualenv/bin/activate;
else
   virtualenv qgisdocs_virtualenv;
   source qgisdocs_virtualenv/bin/activate;
   pip install -r REQUIREMENTS.txt;
fi

make html
deactivate
rsync -uthvr --delete output/ ../output/qgis_core_docs
cd ..

# Getting Desktop documentation

if [ ! -d "desktop-documentation" ]; then 
  git clone --recursive https://github.com/boundlessgeo/desktop-documentation.git;
fi  

cd desktop-documentation/docs;

case "$Version" in
	"1.0")
		git fetch origin r1.0;
		git checkout r1.0;
		git merge origin/r1.0;
		;;
	*)
		git checkout master;
		git pull origin master;
		;;
esac

make html
rsync -uthvr --delete build/ ../../output/desktop_doc

cd ../..

# Appending Plugins Documentation

if [ ! -d "qgis-plugins-documentation" ]; then 
  git clone https://github.com/boundlessgeo/qgis-plugins-documentation.git;
fi 
  
cd qgis-plugins-documentation;
git pull origin master;

paver fetch
paver builddocs
paver deployoffline

rsync -uthvr --delete output/ ../output/plugins

cd ..

#Redirecting links
REGXHTML="output/desktop_doc/html/plugins/supported_plugins.html"
if [[ "${OSTYPE}" =~ ^darwin ]]; then
  sed -i '' -E 's@\.\./\.\./plugins/([[:alnum:]]+)/@../../plugins/\1/index.html@g' ${REGXHTML}
else
  sed -ri "s@\.\./\.\./plugins/(\w*)/@../../plugins/\1/index.html@g" ${REGXHTML}
fi


# Getting Learning Center

#if [ ! -d "connect-learning" ]; then 
#   git clone --recursive https://github.com/boundlessgeo/connect-learning.git;
#fi
#
#cd connect-learning/desktop;
#git pull origin master;
#
#make html-offline
##make get-videos
#rsync -uthvr --delete build/ ../../output/desktop-learning
#cd ../..


#Put index Page in place
cd ..
rsync -uthvr _static/ tmp/output/_static
cp index.html tmp/output
