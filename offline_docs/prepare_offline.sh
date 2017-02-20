# Clean things up
#rm -rf output 
#mkdir output

# Getting QGIS Core Documentation
if [ -d "QGIS-Documentation" ]; then 
  cd QGIS-Documentation;
  git pull origin manual_en_2.14;
else 
  git clone https://github.com/qgis/QGIS-Documentation.git
  cd QGIS-Documentation;
  git fetch origin manual_en_2.14;
fi
git checkout manual_en_2.14
if  [ -d "qgisdocs_virtualenv" ]; then
   source qgisdocs_virtualenv/bin/activate;
else
   virtualenv qgisdocs_virtualenv;
   source qgisdocs_virtualenv/bin/activate;
   pip install -r REQUIREMENTS.txt;
fi
make html
deactivate
rsync -uthvr --delete output/html/en/docs/ ../output/qgis_core_docs
cd ..

# Getting Desktop documentation

if [ -d "desktop-documentation" ]; then 
  cd desktop-documentation;
  git pull origin master;
  cd docs;
else 
  git clone --recursive https://github.com/boundlessgeo/desktop-documentation.git;
  cd desktop-documentation/docs;
fi
make html
cp build/html ../../output/desktop_docs
rsync -uthvr --delete build/html/ ../../output/desktop_doc

cd ../..

# Appending Plugins Documentation

if [ -d "qgis-plugins-documentation" ]; then 
  cd qgis-plugins-documentation;
  git pull origin master;
else 
  git clone https://github.com/boundlessgeo/qgis-plugins-documentation.git;
  cd qgis-plugins-documentation;
fi

paver fetch
paver builddocs
paver deployoffline

rsync -uthvr output/ ../output/plugins

cd ..

#Cleaning up links

sed -ri "s@\.\./\.\./plugins/(\w*)/@../../plugins/\1/index.html@g" output/desktop_doc/plugins/supported_plugins.html

# Getting Learning Center
:'
if [ -d "connect-learning" ]; then 
  cd connect-learning;
  git pull origin master;
else 
  git clone --recursive https://github.com/qgis/QGIS-Documentation.git
  cd connect-learning;
fi
cd desktop
make html-offline
make get-datasets
make get-videos
'

