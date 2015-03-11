# upcoming release milestones and roadmap

## Roadmap

This is an enumeration of thoughts which would be nice to have in gwtquery. The list is intended for both: to be the a base for the team work during the next months, and for contributors in order that they select things to work on.
If you miss something or have suggestions or questions, write your comments and we'll update the page.
If you wanted to contribute let us know sending us an email to the mailing-list.

 1. ~~Improved docs, examples and test coverage~~.
 1. ~~Revise jquery 1.8 api and add some missing methods to gquery (on, off, ...)~~
 1. Add all jquery static utility methods to gQuery.
 1. ~~Rewrite the jquery events system to support customized events, etc.~~
 1. ~~Finish Ajax api~~.
 1. ~~Full implementation of Deferred and Promises. It should work in presenters and JVM~~.
 1. Port most popular jquery plugins to gquery
 1. Review gquery-DnD so as it could use the DnD stuff in gwt-2.4
 1. ~~Make jsQuery almost compatible with jquery so as most popular plugins could be imported as JSNI blocks in gwtquery (builders)~~
 1. jsQuery should support most popular jquery code. A goal should be to support the jquery-ui without importing jquery so as the gquery-ui plugin would not need to import jquery.
 1. ~~Write utility classes to include/exclude code based on browser class~~
 1. ~~Make available js console in all browsers~~.
 1. ~~Utility methods to avoid writing jsni when exporting java code or calling external js~~
 1. We should have a way to automatically wrap jquery-plugins js-api to java. The goal here could be to take gquery-ui as base and produce all the glue code it needs using gwt builders.
 1. Code a script to produce the scaffolding of a new gquery-plugin using a jquery-plugin definition file.
 1. Write a document to help people to produce plugins
 1. ~~Improve test units to the gquery Ajax api~~.
 1. ~~Test whether gquery Ajax works with Cross-Origin Resource Sharing: http://www.nczonline.net/blog/2010/05/25/cross-domain-ajax-with-cross-origin-resource-sharing/~~.
 1. Support $ class whenever gwt releases this fix: http://gwt-code-reviews.appspot.com/1542804/ http://code.google.com/p/google-web-toolkit/issues/detail?id=6799
 1. We could port gquery to Scala-gwt
