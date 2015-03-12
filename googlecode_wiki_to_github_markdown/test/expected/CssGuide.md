# Nice, easy, IDE-friendly and type-safe mechanism to set up css

## Introduction
How many times have you made typo when writing a css property name like _backgroud_ instead of _background_ ?
How many times do you wonder which values can take the _vertical-align_ property or how to correctly set the _list-type_ or _background_ shorthand property ?

GwtQuery proposes a nice, easy, IDE-friendly (i.e. allows your IDE to suggest correct values for selected property) and type-safe way to set up css on your elements or widgets. This is what we will show you in this article.

## CSS scope

GQuery support any CSS2, CSS3 and vendor specific properties to set or retrieve them via the `css()` method, to use in animations, etc.

However, only CSS2 properties (as described [here](http://www.w3.org/TR/CSS21/propidx.html)) are implemented via the type-safe mechanism, although we plan to add CSS3 features in future releases.

## How to get the value of a CSS property
The [CSS](http://gwtquery.googlecode.com/svn/trunk/gwtquery-core/javadoc/com/google/gwt/query/client/css/CSS.html) class lists all available css properties. You can use the properties defined in [CSS](http://gwtquery.googlecode.com/svn/trunk/gwtquery-core/javadoc/com/google/gwt/query/client/css/CSS.html) class with the css() method of GQuery class to get the value of a css property :

```
import static com.google.gwt.query.client.GQuery.$
import com.google.gwt.query.client.css.CSS;
...

//get the background-color of an element with id myId
String myIdBackgroundColor = $("#myId").css(CSS.BACKGROUND_COLOR);

Button myButton = new Button("simple button");
//get border-type of the gwt button
String borderType = $(myButton).css(CSS.BORDER_STYLE);
```

## How to set a value in a CSS property
Each property defined in CSS class proposes different with() methods allowing you to set a value in a type-safe way :

```
//set the border style of the button to 'dotted' value
$(myButton).css(CSS.BORDER_STYLE.with(BorderStyle.DOTTED));

//vertical-align can take a constant value
$("#myId").css(CSS.VERTICAL_ALIGN.with(VerticalAlign.MIDDLE));
//or a length : here 120 px
$("#myId").css(CSS.VERTICAL_ALIGN.with(Length.px(120)));

//it easy now to specify shorthand property...
$("#myId").css(CSS.BACKGROUND.with(
                RGBColor.TRANSPARENT,
                UriValue.url("back.jpg"),
                BackgroundRepeat.NO_REPEAT,
                BackgroundAttachment.SCROLL,
                BackgroundPosition.CENTER));
```

It's now impossible to set wrong value to a property. This code below will not compile :

```
//the value are not specified in the correct order
$("#myId").css(CSS.BACKGROUND.with(
                RGBColor.TRANSPARENT,
                BackgroundRepeat.NO_REPEAT,
                UriValue.url("back.jpg"),
                BackgroundPosition.CENTER,
                BackgroundAttachment.SCROLL));

//the top property accepts only Length value
$("#myId").css(CSS.TOP.with(VerticalAlign.TOP));
```

You can also set several properties in a single call :

```
// specify margin, padding, text-decoration and font-size in one pass
$("#myId").css(CSS.MARGIN.with(Length.px(3)),
               CSS.PADDING.with(Length.px(3), Length.px(5)),
               CSS.TEXT_DECORATION.with(TextDecoration.NONE),
               CSS.FONT_SIZE.with(FontSize.SMALL));
```

## IDE-friendly
The mechanism describe in previous paragraph to set up css is IDE friendly. If you are using an advanced IDE (Eclipse, NetBeans, IntelliJ IDEA ...), it will help you in your css setting :

 * list all css properties available:
<img src="http://gwtquery.googlecode.com/svn/wiki/ide_friendly1.jpg" />

 * vertical-align property can take either a `VerticalAlign` or a `Length`:
<img src="http://gwtquery.googlecode.com/svn/wiki/ide_friendly2.jpg" />

 * list all correct values :
<img src="http://gwtquery.googlecode.com/svn/wiki/ide_friendly3.jpg" />
<img src="http://gwtquery.googlecode.com/svn/wiki/ide_friendly4.jpg" />

## Syntax Alternatives
But GQuery does not force you to use its type-safe syntax, it also propose you other alternatives if you prefer jquery syntax using attribute-value pairs, or if you wanted to 'copy and paste' attributes from a style-sheet document:

```
 $("#myId").css("color", "red");
```

Using javascript property maps:

```
 $("#myId").css($$("top: '50px', left: '25px', color: 'red'"));
```

Or even using the css style sheet syntax:

```
 $("#myId").css($$("margin: 3px; padding: 3px 5px; text-decoration: none; font-size: small;"));
```
