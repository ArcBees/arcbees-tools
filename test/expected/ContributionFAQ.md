# How to contribute in GQuery




## Introduction

Contributions are welcome ! The main goal of this page is to explain a number of points in order to ease contribution in GwtQuery.
This page is a draft and will be improved in the future.


## How to import the source code into your IDE ?

Before to start contributing, you have to import the source code of GwtQuery inside your favorite IDE. This section will the different steps to import the GwtQuery code in Eclipse. If you are not using Eclipse as IDE, you should easily adapt this section to your IDE.

  * Be sure you have installed git and maven and both 'mvn' and 'git' commands are in your path.

```
$ mvn -version
Apache Maven 3.0.3 ...
$ git --version
git version 1.7.5.4
```


  * Checkout the project and change into the new folder created

```
$ git clone git@github.com:gwtquery/gwtquery.git
$ cd gwtquery/gwtquery-core
```


  * Normally developers run tests to assure that they don't break anything after doing any change. Nevertheless, since gQuery makes an intensive use of GWTTestCase you could have problems in your platform . We checkout periodically the code and run tests in a linux platform and if something goes wrong we fix it. If you cannot run gQuery tests, don't hesitate to continue working on the code and just notice other developers before sending a new pull request that you couldn't run tests.

To run gQuery tests, do it twice, the first time ignore the error related with gwt-unitCache, it will not happen the second time.

```
$ mvn test
...
Unable to create new cache log file /msoft/android/gwtquery/war/../gwt-unitCache/gwt-unitCache-000001336DBA483E.
...
Tests run: 155, Failures: 0, Errors: 0, Skipped: 0
...
BUILD SUCCESS
...

$ mvn test
...
BUILD SUCCESS
...
```


  * Install eclipse and these plugins:
    * Google plugin for eclipse (update-site: http://dl.google.com/eclipse/plugin/3.7 or 3.6 or 3.5)
    * Sonatype Maven plugin (update-site: http://m2eclipse.sonatype.org/site/m2e)

  * Import the maven project via the menu `File -> Import -> Maven -> Existing Maven Projects`

## How to run test ?
To run test, you can either use maven in the source folder

```
$ cd gwtquery-core
$ mvn test
```

or by using Eclipse. Click right on any file under the src/test/java/com/google/gwt/query folder. If the file ends with TestGWT.java,  choose `run as -> GWT junit test` otherwise choose `run as -> junit test`

If you want to know the coverage, you could install the eclipse plugin `EclEmma java code coverage` eclipse plugin and run `Coverage as -> jUnit Test`

## Code style and formating
GwtQuery follows the same rules/conventions than GWT regarding the code styling and formatting. These conventions can be found in this [page](http://code.google.com/webtoolkit/makinggwtbetter.html#codestyle). Please, follow these rules before committing your code !!

## How to submit your code ?

Whether it is to solve an issue or suggest a new features, there are two ways to submit your code:

 1. Preferred: clone the code in [github](https://github.com/gwtquery/gwtquery), and send a pull request with your changes. There are lots of posts helping how to use github and submit pull requests.
 1. Alternative: open an [issue](https://github.com/gwtquery/gwtquery/issues?state=open) and attach your patch to it. Use git in command line to create your patch:

```
$ git diff > ~/fix_issue_123.diff
```
