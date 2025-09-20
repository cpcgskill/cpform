# cpform.docker API Reference

The `cpform.docker` module is responsible for creating and managing CPForm interface windows. It provides various window container types (dialogs, popup menus, standard windows, etc.), automatically handles cross-platform Qt compatibility and DCC software integration.

<div style="display: flex; justify-content: space-between;">
  <div>
    <a href="./docker.en-US.md">English</a> | <a href="./docker.zh-CN.md">中文</a>
  </div>
</div>

## Table of Contents

- [API Quick Reference](#api-quick-reference)
- [Window Container Functions](#window-container-functions)
- [Window Management Functions](#window-management-functions)

## API Quick Reference

### Window Container Functions

| Function | Purpose | Features |
|----------|---------|----------|
| `dialog_docker()` | Modal dialog | Blocks interaction, must be handled |
| `popup_menu_docker()` | Popup menu | Auto-close, lightweight |
| `default_docker()` | Standard window | Reusable, supports updates |
| `middle_docker()` | Centered window | Content centered, with header (deprecated) |
| `scalable_view_docker()` | Scalable view | Supports scaling (testing) |
| `widget_docker()` | Widget container | Embedded, no independent window |

### Window Management Functions

| Function | Purpose | Description |
|----------|---------|-------------|
| [`get_docker(name)`](#get_docker) | Get window | Returns window instance or None |
| [`close_docker(name)`](#close_docker) | Close window | Hide window, keep instance |
| [`delete_docker(name)`](#delete_docker) | Delete window | Completely destroy window instance |
| [`quit_dialog_docker()`](#quit_dialog_docker) | Exit dialog | Close current modal dialog |

### Common Parameters

- `form` (QWidget): CPForm form object or QWidget
- `icon` (str): Window icon path, optional
- `title` (str): Window title, optional  
- `name` (str): Window name for management, optional
- `size` (tuple): Window size (width, height), optional
- `pos` (QPoint): Display position, popup menu only
- `close_callback` (callable): Close callback function, optional

### Exceptions

- `CPMelFormException`: Raised when window operations fail

## Window Container Functions

### dialog_docker()

Create and display a modal dialog.

```python
def dialog_docker(form, icon=None, title='Window'):
    """
    Create modal dialog window
    
    :type form: QWidget
    :param form: CPForm form object
    :type icon: str
    :param icon: Window icon path
    :type title: str
    :param title: Window title
    :rtype: DialogDocker
    :return: Dialog instance
    """
```

**Use Cases:**
- Settings dialogs
- Confirmation prompts
- Interfaces that require user attention

### popup_menu_docker()

Create a popup menu window.

```python
def popup_menu_docker(form, pos=None, from_widget=None, close_callback=None):
    """
    Create popup menu window
    
    :type form: QWidget
    :param form: CPForm form object
    :type pos: QPoint
    :param pos: Display position, defaults to mouse position
    :type from_widget: QWidget
    :param from_widget: Reference widget, menu will appear below it
    :type close_callback: callable
    :param close_callback: Close callback function
    :rtype: DockerWarp
    :return: Wrapper object with delete_docker() method
    """
```

**Use Cases:**
- Right-click context menus
- Dropdown menus
- Tooltip windows

### default_docker()

Create or update default window.

```python
def default_docker(icon=None, name="Window", title=None, form=tuple(), size=None):
    """
    Create or update default window
    
    :type icon: str
    :param icon: Window icon path
    :type name: str
    :param name: Window name (used for window management)
    :type title: str
    :param title: Window title, defaults to name
    :type form: QWidget
    :param form: CPForm form object
    :type size: tuple
    :param size: Window size (width, height)
    """
```

**Features:**
- If a window with the same name already exists, updates content instead of creating new window
- Window is added to global window table for management
- Most commonly used window creation method

### middle_docker()

Create a centered display window.

```python
def middle_docker(icon=None, name="Window", title=None, form=tuple(), size=None):
    """
    Create centered display window
    
    :type icon: str
    :param icon: Window icon path
    :type name: str
    :param name: Window name
    :type title: str
    :param title: Window title
    :type form: QWidget
    :param form: CPForm form object
    :type size: tuple
    :param size: Window size
    """
```

**Note:** <div style="color: yellow">This feature is deprecated, recommend using `default_docker()` instead.</div>

### scalable_view_docker()

Create a scalable view window.

```python
def scalable_view_docker(icon=None, name="Window", title=None, form=tuple(), size=None,
                        min_scale=0.2, max_scale=5.0, scale_factor=1.2):
    """
    Create scalable view window
    
    :type icon: str
    :param icon: Window icon path
    :type name: str
    :param name: Window name
    :type title: str
    :param title: Window title
    :type form: QWidget
    :param form: CPForm form object
    :type size: tuple
    :param size: Window size
    :type min_scale: float
    :param min_scale: Minimum scale ratio
    :type max_scale: float
    :param max_scale: Maximum scale ratio
    :type scale_factor: float
    :param scale_factor: Scale factor
    """
```

**Note:** <div style="color: yellow">This feature is in testing phase and may have some issues.</div>

### widget_docker()

Create a widget container.

```python
def widget_docker(form=tuple(), parent=None):
    """
    Create widget container
    
    :type form: QWidget
    :param form: CPForm form object
    :type parent: QWidget
    :param parent: Parent window
    :rtype: WidgetDocker
    :return: Widget container instance
    """
```

## Window Management Functions

### get_docker()

Get window instance by name.

```python
def get_docker(name, default=None):
    """
    Get window instance
    
    :type name: str
    :param name: Window name
    :param default: Default return value
    :return: Window instance or default value
    """
```

### close_docker()

Close specified window.

```python
def close_docker(name="Window"):
    """
    Close specified window
    
    :type name: str
    :param name: Window name
    :raises CPMelFormException: Raised when window doesn't exist
    """
```

### delete_docker()

Delete specified window.

```python
def delete_docker(name="Window"):
    """
    Delete specified window (close and remove from memory)
    
    :type name: str
    :param name: Window name
    :raises CPMelFormException: Raised when window doesn't exist
    """
```

### quit_dialog_docker()

Close current active dialog.

```python
def quit_dialog_docker():
    """
    Close current active modal dialog
    """
```