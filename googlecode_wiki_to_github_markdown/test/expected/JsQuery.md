# GQuery exported to javascript.

## Introduction

JsQuery is a project with allows to export gQuery methods and objects to javascript, so as we can produce a library which could be used as a replacement of jQuery.

The goal is not to compete against jquery, but to avoid including jquery in Gwt applications which require jquery code (ie: jquery plugins, designers code, etc).

It is also a research work demonstrating that any javascript API could be developed in java and exported to javascript, and jQuery is a good use case, since it is arguably the js API most widely used.

We use the [gwt-exporter](http://code.google.com/p/gwt-exporter/) library, which is able to expose Gwt classes and methods to javascript using annotations.

The main goal for us, is to encourage people to wrap jQuery plugins, just including them as jsni and creating java wrappers methods around it. Maybe in the future we could have code generators to get a jquery plugin and wrap it for using with gquery.

## Issues

Right now most jquery prototype methods are exposed but we still have to implement many of the jquery static methods.

Gwt-exporter introduces a high amount of extra code to deal with types and wrappers.

Gwt-exporter penalizes performance since it spends time figuring out which methods to call, and how to wrap parameters and returned objects.

## Javascript Usage

* Experimental !!! *

To use jsQuery as a replacement of jQuery in a non GWT project, just replace the `src` attribute in the script tag importing jQuery by the url with jsquery.js, and use it as habitual (see Known issues below).

```

// Just replace jquery by jsquery
<!-- <script src="http://code.jquery.com/jquery-latest.min.js" /> -->
<script src="http://gwtquery.googlecode.com/svn/api/jsquery.js" />

// Write your code as habitual, but be sure you wrap it in a ready function
<script type="text/javascript">
  $(document).ready(function(){
    [...]
  });
</script>
```

[Here](http://gwtquery.googlecode.com/svn/api/samples/zoom.html) you can see an example page where we have just replaced the original jquery.js library by the jsquery.js produced from gquery.

## Wrapping jQuery code in Gwt

* Experimental !!! *

In order to use a jquery plugin in a GWT project, you have to:
 1. Include the gwtexporter dependency in your project. In the case of maven:

```
  <dependency>
     <groupId>org.timepedia.exporter</groupId>
     <artifactId>gwtexporter</artifactId>
     <version>2.4.0-SNAPSHOT</version>
     <scope>provided</scope>
  </dependency>
```

 1. Inherit gwtexporter in your gwt.xml file

```
  <inherits name='org.timepedia.exporter.Exporter' />
  <set-property name="export" value="yes" />
```

 1. Copy the classes [GQueryOverlay.java](http://code.google.com/p/gwtquery/source/browse/jsquery/src/main/java/com/google/gwt/query/jsquery/client/GQueryOverlay.java) and [JsQueryUtils.java](http://code.google.com/p/gwtquery/source/browse/jsquery/src/main/java/com/google/gwt/query/jsquery/client/JsQueryUtils.java) to your plugin project.
 1. Add these lines in your entry point class:

```
  public void onModuleLoad() {
  [...]
    // Export jsQuery api
    OverlayGQuery.export();

    // Export or initialize the plugins
    [...]

    // Optional: Run the $(document).ready() code you added to your page
    OverlayGQuery.onLoad();
  [...]
  }

```

 1. Then you can do either: import the jquery javascript code in your html, or wrap it in a a java class copying the javascript in a jsni method:

```

public abstract class MyPlugin {
  public static native void loadPlugin() /*-{
   // Set these variables so as your plugin references the appropriate objects
   var jQuery = $wnd.$;
   var window = $wnd;
   var document = $doc;

   // Paste the plugin code here
   (function($)
   {
    [...]
   })(jQuery);
  }-*/
}

public void onModuleLoad() {
  [...]
    MyPlugin.loadPlugin();
  [...]
}

```

 1. Finally check which things of your code fails and try to get a different way to do that, or send patches to gquery team in order to improve the jsQuery api.
   * You can see an example of jquery plugin wrapped [here](http://code.google.com/p/gwtquery/source/browse/jsquery/src/main/java/gwtquery/jsplugins/menu/client/JsMenu.java)
   * [Here](http://code.google.com/p/gwtquery/source/browse/jsquery/src/main/java/gwtquery/jsplugins/menu/client/jsmenu.diff) you have the small differences we had to apply to make it work.
 1. The last step in your plugin should be to populate js methods in the plugin to java, right now you could take a look to gwtquery-ui until we summarize that.
