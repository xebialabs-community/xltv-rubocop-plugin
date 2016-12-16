# XL TestView Rubocop plugin #

## Preface ##

This plugin will parse [Rubocop](https://github.com/bbatsov/rubocop) json results files and report them in XL TestView


## CI status ##

[![Build Status][xltv-rubocop-plugin-travis-image] ][xltv-rubocop-plugin-travis-url]
[![Build Status][xltv-rubocop-plugin-codacy-image] ][xltv-rubocop-plugin-codacy-url]
[![Build Status][xltv-rubocop-plugin-code-climate-image] ][xltv-rubocop-plugin-code-climate-url]


[xltv-rubocop-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xltv-rubocop-plugin.svg?branch=master
[xltv-rubocop-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xltv-rubocop-plugin
[xltv-rubocop-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/4ccbfe085e53497ca0df627521b6855b
[xltv-rubocop-plugin-codacy-url]: https://www.codacy.com/app/rvanstone/xltv-rubocop-plugin
[xltv-rubocop-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xltv-rubocop-plugin/badges/gpa.svg
[xltv-rubocop-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xltv-rubocop-plugin


## Usage ##

To use this plugin:

* Using gradle and Docker: `./gradlew runDocker`
* Using an existing XL TestView installation:
  1. Move the [jar file](https://github.com/xebialabs-community/xltv-rubocop-plugin/releases) into the /plugins directory of your XL TestView server installation
  2. Restart XL TestView if it's already running

You will now be able to import Rubocop results. Enter the import directory as the root folder where your Rubocop files are saved. 
For example if you have multiple results such as Res1, Res2, Res3, use the directory where those folders are stored.


## References ##
+ [Rubocop](https://github.com/bbatsov/rubocop)
+ [Rubocop docs](http://rubocop.readthedocs.io/en/latest/)


