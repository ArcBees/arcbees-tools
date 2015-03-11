# How to write new gquery plugins

## Introduction

GQuery supports a Plugin system for extension of the core GQuery object.

You could either code plugins in your application which extends the GQuery features, or create new libraries which could be used in different applications.

To create a new plugin and export it as a separated library, you have the [gquery-plugin-archetype](http://code.google.com/p/gwtquery-plugins/downloads/detail?name=gquery-plugin-archetype-0.3-SNAPSHOT.jar&can=2&q=#makechanges), a maven archetype which creates all necessary stuff to easily start up a new plugin.

If you wanted to share it with the community you should read the [HostingPlugins](http://code.google.com/p/gwtquery-plugins/wiki/HostingPlugins) page in the [gwtquery-plugins](http://code.google.com/p/gwtquery-plugins) project.

## Details

### Writing a plugin
It is simple to create a new plugin in your application, just create a new java class extending `GQuery`, and register it in the plugin system.

As you can see in the example code bellow you have to:
 * Create a static reference to the plugin class literal to facilitate the use of the plugin (this is just a convention).
 * Register the plugin in a static way so as `GQuery` knows about the plugin (it is mandatory)
 * Next, you have to create a constructor for your plugin accepting a `GQuery` object.
 * And finally, you can either write new public methods which will extend `GQuery` abilities, or override its methods to change or improve the default behavior.

```
public class MyPlugin extends GQuery {

  // Register the plugin in GQuery plugin system and
  // set a shortcut to the class
  public static final Class<MyPlugin> MyPlugin = GQuery.registerPlugin(
    MyPlugin.class, new Plugin<MyPlugin>() {
      public MyPlugin init(GQuery gq) {
        return new MyPlugin(gq);
      }
    });

  // Initialization
  public MyPlugin(GQuery gq) {
    super(gq);
  }

  // Add a new method to GQuery objects
  public MyPlugin newMethod() {
    // Write your code here
    return this;
  }

  // Override the default behavior of GQuery existing methods
  public MyPlugin clear() {
    super.clear();
    // Write your code here.
    return this;
  }

```

### Using the plugin
To use the plugin, you must do two things:

first, statically import a reference to the Plugin's class literal,

```
import static MyPlugin.MyPlugin;
```

and secondly, invoke the method `as` which converts the basic GQuery interface into an instance of the plugin interface

```
$("h1").as(MyPlugin).newMethod();
```

The `as` method will return an instance of the new class `MyPlugin` with the same matched elements.

GQuery plugins are required to inherit from the `GQuery` class itself, so a plugin encapsulates all of the methods of the GQuery object, as well as introducing new methods.
