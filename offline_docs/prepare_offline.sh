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
#	"1.1")
#		git fetch origin r1.1;
#		git checkout r1.1;
#		git merge origin/r1.1;
#		;;
	*)
		git checkout master;
		git pull origin master;
		;;
esac

echo "Setting up virtual enviornment..."

if [ -d "bdeskdocs_virtualenv" ]; then
   rm -rf bdeskdocs_virtualenv
fi

virtualenv bdeskdocs_virtualenv;
source bdeskdocs_virtualenv/bin/activate;
pip install -r requirements.txt;

make html
deactivate
rsync -uthvr --delete build/ ../../output/desktop_doc

cd ../..

#Appending Plugins Documentation

if [ ! -d "qgis-plugins-documentation" ]; then
  git clone https://github.com/boundlessgeo/qgis-plugins-documentation.git;
fi

cd qgis-plugins-documentation;
git pull origin master;

paver fetch
paver builddocs -r
paver deployoffline

rsync -uthvr --delete output/ ../output/plugins

cd ..

#Rename folders for expected names in docs
mv output/plugins/master output/plugins/masterpasshelper
mv output/plugins/mgrs output/plugins/mgrstools
mv output/plugins/reports output/plugins/supporttool

#Redirecting links
REGXHTML="output/desktop_doc/html/plugins/supported_plugins.html"
if [[ "${OSTYPE}" =~ ^darwin ]]; then
  sed -i '' -E 's@\.\./\.\./plugins/([[:alnum:]]+).*\"/@../../../plugins/\1/index.html"@g' ${REGXHTML}
else
  sed -ri 's@\.\./\.\./plugins/(\w+).*\"@../../../plugins/\1/index.html"@g' ${REGXHTML}
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

# Getting QGIS Core Documentation

if [ ! -d "QGIS-Documentation" ]; then
  git clone https://github.com/qgis/QGIS-Documentation.git;
fi
cd QGIS-Documentation;

rm -rf output;
git checkout -- .
case "$Version" in
	"1.0")
		git fetch origin manual_en_2.14;
		git checkout manual_en_2.14;
		git merge origin/manual_en_2.14;
		;;
	"1.1")
	    git fetch origin release_2.18;
		git checkout release_2.18;
		git merge origin/release_2.18;
		;;
	*)
		git checkout master;
		git pull origin master;
		;;
esac

echo "Setting up virtual enviornment..."

if [ -d "qgisdocs_virtualenv" ]; then
   rm -rf qgisdocs_virtualenv
fi

virtualenv qgisdocs_virtualenv;
source qgisdocs_virtualenv/bin/activate;
pip install -r REQUIREMENTS.txt;

# Exclude unwanted QGIS Documentation
echo "Replacing conf.py file..."

ARRAY=("training_manual" "developers_guide" "documentation_guidelines" "gentle_gis_introduction")

for doc in ${ARRAY[*]}
do
  sed -i.bak "s|#exclude_patterns += \['docs/${doc}|exclude_patterns += \['docs/${doc}|g" source/conf.py;
done

sed -i.bak2 '/PDF/d' source/docs/index.rst;

make fasthtml
deactivate
rsync -uthvr --delete output/ ../output/qgis_core_docs
cd ..

#Put index Page in place
cd ..
rsync -uthvr _static/ tmp/output/_static
cp index.html tmp/output
