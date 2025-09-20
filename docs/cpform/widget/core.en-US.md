# cpform.widget.core Reference

The `cpform.widget.core` module provides declarative UI components, including basic controls, layout containers, buttons, input fields, etc. All components support unified style themes and data reading interfaces.

<div style="display: flex; justify-content: space-between;">
  <div>
    <a href="./core.en-US.md">English</a> | <a href="./core.zh-CN.md">中文</a>
  </div>
</div>

## Table of Contents

- [Basic Components](#basic-components)
- [Text Components](#text-components)
- [Input Components](#input-components)
- [Button Components](#button-components)
- [Layout Components](#layout-components)
- [Container Components](#container-components)
- [Interactive Components](#interactive-components)
- [Quick Reference](#quick-reference)

## Basic Components

### Widget

Base class for all CPForm components, providing common mouse event handling and data interfaces.

```python
class Widget(QWidget, FormInterface):
    def __init__(self, 
                 left_clicked_callback=None,
                 right_clicked_callback=None,
                 min_width=None, min_height=None,
                 max_width=None, max_height=None,
                 size_policy_width=None, size_policy_height=None,
                 fixed_width=None, fixed_height=None)
```

**Parameters:**
- `left_clicked_callback` (callable): Left click callback
- `right_clicked_callback` (callable): Right click callback
- `min_width/min_height` (int): Minimum width/height
- `max_width/max_height` (int): Maximum width/height
- `fixed_width/fixed_height` (int): Fixed width/height

### Warp / WarpWidget

Wrapper component for wrapping other components.

```python
def Warp(child, **kwargs):
    """Wrap child component"""
```

### Background / BackgroundWidget

Container component with background.

```python
def Background(child, color=cf_config.BackgroundColor, round_corners=cf_config.RoundCornersLevel3, style='Rounded', **kwargs):
    """
    Create container with background
    
    :param child: Child component
    :param color: Background color
    :param round_corners: Corner radius size
    :param style: Style 'Rounded' | 'Capsule'
    """
```

### ToggleWidget

Generic container for switchable content.

```python
def ToggleWidget(widget=None, **kwargs):
    """Switchable container component"""
    
# Methods
def toggle_to(widget):
    """Switch to specified component"""
```

## Text Components

### Label / LabelWidget

Text label component.

```python
def Label(text='', word_wrap=False, font_size=None, align=None, text_color=cf_config.NormalTextColor, **kwargs):
    """
    Text label
    
    :param text: Display text
    :param word_wrap: Whether to wrap text automatically
    :param font_size: Font size
    :param align: Alignment 'left'|'center'|'right'
    :param text_color: Text color
    """
```

### Heading Components

```python
def H1(text='', **kwargs):  # 72px
def H2(text='', **kwargs):  # 59px  
def H3(text='', **kwargs):  # 47px
def H4(text='', **kwargs):  # 36px
def H5(text='', **kwargs):  # 27px
def H6(text='', **kwargs):  # 19px
```

### Help / HelpWidget

Help text component with automatic text wrapping.

```python
def Help(text='', **kwargs):
    """Help text component"""
```

## Input Components

### LineEdit / LineEditWidget

Single-line text input field.

```python
def LineEdit(text='', is_encrypt=False, placeholder_text='', tool_tip='', 
             return_pressed_callback=None, validator=None, **kwargs):
    """
    Single-line text input
    
    :param text: Initial text
    :param is_encrypt: Whether to encrypt display (password input)
    :param placeholder_text: Placeholder text
    :param tool_tip: Tooltip
    :param return_pressed_callback: Enter key callback
    :param validator: Validator (QValidator or regular expression)
    """
```

**Methods:**
- `set_text(text)`: Set text
- `get_text()`: Get text
- `read_data()`: Returns [text]

### Special Input Fields

```python
def IntegerLineEdit(*args, **kwargs):
    """Integer input field with automatic integer format validation"""
    
def FloatLineEdit(*args, **kwargs):
    """Float input field with automatic float format validation"""
    
def EmailLineEdit(*args, **kwargs):
    """Email input field with automatic email format validation"""
```

### Slider Components

```python
def IntSlider(min=0, max=100, default=0, **kwargs):
    """
    Integer slider
    
    :param min: Minimum value
    :param max: Maximum value  
    :param default: Default value
    """

def FloatSlider(min=0, max=1, default=0, **kwargs):
    """Float slider"""
```

### CheckBox / CheckBoxWidget

Checkbox component.

```python
def CheckBox(info="", default_state=False, update_func=None, **kwargs):
    """
    Checkbox
    
    :param info: Display text
    :param default_state: Default checked state
    :param update_func: State change callback
        update_func: State change callback
    """
```

**Methods:**
- `set_state(state)`: Set state
- `state()`: Get state
- `read_data()`: Returns [bool]

## Button Components

### Button / ButtonWidget

Basic button component.

```python
def Button(text='', icon=None, icon_size=None, func=None, color=None, text_color=None, **kwargs):
    """
    Basic button
    
    :param text: Button text
    :param icon: Icon name (from feather icon set)
    :param icon_size: Icon size
    :param func: Click callback function
    :param color: Background color
    :param text_color: Text color
    """
```

### Preset Style Buttons

```python
def PrimaryButton(**kwargs):    # Primary button (blue)
def AttentionButton(**kwargs): # Attention button (bright blue)
def SuccessButton(**kwargs):   # Success button (green)
def WarningButton(**kwargs):   # Warning button (yellow)
def ErrorButton(**kwargs):     # Error button (red)
def NormalButton(**kwargs):    # Normal button (gray)
```

## Layout Components

### HBoxLayout

Horizontal layout container.

```python
def HBoxLayout(childs, margins=5, spacing=cf_config.Spacing, align=None, **kwargs):
    """
    Horizontal layout
    
    :param childs: List of child components
    :param margins: Margins (int or [left,top,right,bottom])
    :param spacing: Component spacing
    :param align: Alignment
    """
```

### VBoxLayout

Vertical layout container.

```python
def VBoxLayout(childs, margins=5, spacing=cf_config.Spacing, align=None, **kwargs):
    """Vertical layout
    
    :param childs: List of child components
    :param margins: Margins (int or [left,top,right,bottom])
    :param spacing: Component spacing
    :param align: Alignment
    """
```

### FormLayout

Form layout container.

```python
def FormLayout(childs, margins=5, spacing=cf_config.Spacing, align=None, **kwargs):
    """
    Form layout
    
    :param childs: [label1, widget1, label2, widget2, ...] Alternating labels and components
    :param margins: Margins (int or [left,top,right,bottom])
    :param spacing: Component spacing
    :param align: Alignment
    """
```

## Container Components

### ScrollArea / ScrollAreaWidget

Scroll area container.

```python
def ScrollArea(widget, hide_scroll_bar=False, **kwargs):
    """
    Scroll container
    
    :param widget: Content component
    :param hide_scroll_bar: Whether to hide scroll bar
    """
```

### Collapse / CollapseWidget

Collapsible container.

```python
def Collapse(body, text='', default_state=False, **kwargs):
    """
    Collapsible container
    
    :param body: Body content component
    :param text: Collapse title
    :param default_state: Default state (False=collapsed, True=expanded)
    """
```

## Interactive Components

### SubmitWidget

Form submission container that automatically collects child component data.

```python
def SubmitWidget(form=tuple(), func=lambda *args: 0, doit_text="Apply", 
                 margins=5, spacing=cf_config.Spacing, align=None, **kwargs):
    """
    Form submission container
    
    :param form: List of form components
    :param func: Function called on submission, receives all component data
    :param doit_text: Submit button text
    :param margins: Margin settings
    :param spacing: Component spacing
    :param align: Alignment
    """
```

**Methods:**
- `doit_value()`: Get data from all child components
- `doit()`: Trigger submission operation

## Quick Reference

### Component Categories

| Type | Components | Purpose |
|------|------------|---------|
| **Basic** | `Widget`, `Warp`, `Background`, `ToggleWidget` | Basic containers and wrappers |
| **Text** | `Label`, `H1`~`H6`, `Help` | Text display |
| **Input** | `LineEdit`, `IntegerLineEdit`, `FloatLineEdit`, `EmailLineEdit` | Text input |
| **Slider** | `IntSlider`, `FloatSlider` | Numeric selection |
| **Selection** | `CheckBox` | Boolean selection |
| **Button** | `Button`, `PrimaryButton`, `SuccessButton`, etc. | Action triggers |
| **Layout** | `HBoxLayout`, `VBoxLayout`, `FormLayout` | Component arrangement |
| **Container** | `ScrollArea`, `Collapse`, `SubmitWidget` | Content organization |

### Common Parameters

**Size Control:**
- `min_width`, `min_height`: Minimum size
- `max_width`, `max_height`: Maximum size
- `fixed_width`, `fixed_height`: Fixed size

**Layout Parameters:**
- `margins`: Margins, can be integer or [left,top,right,bottom]
- `spacing`: Component spacing
- `align`: Alignment ('left', 'center', 'right', 'top', 'bottom')

**Callback Functions:**
- `func`: Button click callback
- `update_func`: State change callback
- `return_pressed_callback`: Enter key callback
- `left_clicked_callback`: Left click callback
- `right_clicked_callback`: Right click callback

### Data Interface

All components implement `read_data()` method:

```python
# Input components return input values
line_edit.read_data()  # ['text']
check_box.read_data()  # [True/False]
slider.read_data()     # [number]

# Container components return generator of child component data
layout.read_data()     # Generator, iterates through all child component data
```

### Style Customization

```python
# Custom colors
Button(color='#ff0000', text_color='#ffffff')
Background(color='#333333')

# Custom fonts
Label(font_size=16, text_color='#666666')

# Custom corners
Background(round_corners=10, style='Capsule')
```

### Common Combinations

```python
# Form row
FormLayout([
    'Username:', LineEdit(),
    'Password:', LineEdit(is_encrypt=True),
])

# Button group
HBoxLayout([
    PrimaryButton(text='OK', func=confirm),
    NormalButton(text='Cancel', func=cancel),
])

# Settings panel
Collapse(
    VBoxLayout([
        CheckBox('Enable Feature'),
        IntSlider(0, 100, 50),
        LineEdit(placeholder_text='Enter path'),
    ]),
    text='Advanced Settings'
)
```