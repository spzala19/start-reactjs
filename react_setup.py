import os
import webbrowser
#==== initalize npm project ====
os.system("npm init -y")
#creates package.json

#== install react =====
os.system("npm install react react-dom")
#installs node modules

#==== add code formatter =======
os.system("npm install prettier")
# command to format single file : npx prettier --write script.js
# create .prettierrc file for config

#===== add eslint for uniform coding style amoung team members ========
os.system("npm install -D eslint eslint-config-prettier")
# cammand to lint : eslint \"src/**/*.{js,jsx}\" --quiet
# create .eslintrc.json file for config
#install following modules
os.system("npm install eslint-plugin-import@latest --save-dev")
os.system("npm install eslint-plugin-react@latest --save-dev")
os.system("npm install eslint-plugin-jsx-a11y@latest --save-dev")
os.system("npm install -D eslint-config-airbnb")
os.system("npm install eslint-plugin-react-hooks@latest --save-dev")

#==== Install parcle (alternetive for webpack)
os.system("npm install -D parcel-bundler")

#==== Content of files ================================================================#
#===== Add .gitignore file
git = """
node_modules
.cache/
dist/
.env
.DS_Store
coverage/
.vscode/"""
#=== .prettierrc.json file 
pretty = """
{
    "singleQuote": true
}
"""
#===== .eslintrc.json file
eslint = """
{
    "extends":[
        "eslint:recommended",
        "plugin:import/errors",
        "plugin:react/recommended",
        "plugin:jsx-a11y/recommended",
        "prettier",
        "prettier/react",
        "airbnb"],
        "rules":{
            "react/prop-types":0,
            "react/jsx-filename-extension": [1, { "extensions": [".js", ".jsx"] }],
            "react-hooks/rules-of-hooks": "error",
            "react-hooks/exhaustive-deps":1,
            "no-console":1,
            "no-sequences":"off"
        },
    "plugins":["react","import","jsx-a11y","react-hooks"],
    "parserOptions":{
        "ecmaVersion":11,
        "sourceType":"module",
        "ecmaFeatures":{
            "jsx":true
        }
    },
    "env": {
        "browser": true,
        "es2020": true,
        "node": true
    },
    "settings":{
        "react":{
            "version":"detect"
        }
    }
}
"""
#index.html
indexHtml = """
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet/css" href="style.css" />
  </head>
  <body>
    <div id="root">content not rendered</div>
    <script src="./App.js"></script>
  </body>
</html>
"""
#App.js
appJs = """
import React from 'react';
import ReactDOM from 'react-dom';

const App = () => (
  <div>
    <p>dekh liya? AA gaya swad?</p>
  </div>
);
ReactDOM.render(<App />, document.getElementById('root'));

"""
#style.css
styleCss = ''
#======================= generating files ========================================
filedict = {'.gitignore':git,'.prettierrc.json':pretty,'.eslintrc.json':eslint,'src/index.html':indexHtml,'src/App.js':appJs,'src/style.css':styleCss}
os.system("mkdir src")
for fil in filedict:
    print(fil)
    with open(fil,'+w') as rw:
        rw.write(filedict[fil])

#==================== updating package file =========
name,version,description = "xyz","1.0.0","hello"
import json

#=== package.json
a_file = open("package.json", "r")
json_object = json.load(a_file)
a_file.close()

a_file = open("package.json", "w")
json_object['name'] = name
json_object['version'] = version
json_object['description'] = description
json_object['scripts']['format'] = "prettier \"src/**/*.{js,html}\" --write"
json_object['scripts']['lint'] = "eslint \"src/**/*.{js,jsx}\" --quiet"
json_object['scripts']['dev'] = "parcel src/index.html"

json.dump(json_object, a_file,indent=2)
a_file.close()

#===== package-lock.json
a_file = open("package-lock.json", "r")
json_object = json.load(a_file)
a_file.close()

a_file = open("package-lock.json", "w")
json_object['name'] = name
json_object['version'] = version

json.dump(json_object, a_file,indent=2)
a_file.close()

os.system("npm run format")
os.system("npm run lint -- --fix")
os.system("npm run dev")
