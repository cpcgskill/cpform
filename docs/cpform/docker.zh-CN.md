# cpform.docker API 参考

`cpform.docker` 模块负责创建和管理 CPForm 界面窗口。提供多种窗口容器类型（对话框、弹出菜单、标准窗口等），自动处理跨平台 Qt 兼容性和 DCC 软件集成。

<div style="display: flex; justify-content: space-between;">
  <div>
    <a href="./docker.en-US.md">English</a> | <a href="./docker.zh-CN.md">中文</a>
  </div>
</div>

## 目录

- [API 快速参考](#api-快速参考)
- [窗口容器函数](#窗口容器函数)
- [窗口管理函数](#窗口管理函数)

## API 快速参考

### 窗口容器函数

| 函数 | 用途 | 特点 |
|-----|------|------|
| `dialog_docker()` | 模态对话框 | 阻塞交互，必须处理 |
| `popup_menu_docker()` | 弹出菜单 | 自动关闭，轻量级 |
| `default_docker()` | 标准窗口 | 可重用，支持更新 |
| `middle_docker()` | 居中窗口 | 内容居中，带头部(弃用) |
| `scalable_view_docker()` | 缩放视图 | 支持缩放(测试) |
| `widget_docker()` | Widget容器 | 嵌入式，无独立窗口 |

### 窗口管理函数

| 函数 | 用途 | 说明 |
|-----|------|------|
| [`get_docker(name)`](#get_docker) | 获取窗口 | 返回窗口实例或None |
| [`close_docker(name)`](#close_docker) | 关闭窗口 | 隐藏窗口，保留实例 |
| [`delete_docker(name)`](#delete_docker) | 删除窗口 | 完全销毁窗口实例 |
| [`quit_dialog_docker()`](#quit_dialog_docker) | 退出对话框 | 关闭当前模态对话框 |

### 常用参数

- `form` (QWidget): CPForm 表单对象或 QWidget
- `icon` (str): 窗口图标路径，可选
- `title` (str): 窗口标题，可选  
- `name` (str): 窗口名称，用于管理，可选
- `size` (tuple): 窗口大小 (width, height)，可选
- `pos` (QPoint): 显示位置，仅弹出菜单使用
- `close_callback` (callable): 关闭回调函数，可选

### 异常

- `CPMelFormException`: 窗口操作失败时抛出

## 窗口容器函数

### dialog_docker()

创建并显示模态对话框。

```python
def dialog_docker(form, icon=None, title='Window'):
    """
    创建模态对话框窗口
    
    :type form: QWidget
    :param form: CPForm 表单对象
    :type icon: str
    :param icon: 窗口图标路径
    :type title: str
    :param title: 窗口标题
    :rtype: DialogDocker
    :return: 对话框实例
    """
```

**使用场景：**
- 设置对话框
- 确认提示框
- 需要用户必须处理的界面

### popup_menu_docker()

创建弹出式菜单窗口。

```python
def popup_menu_docker(form, pos=None, from_widget=None, close_callback=None):
    """
    创建弹出菜单窗口
    
    :type form: QWidget
    :param form: CPForm 表单对象
    :type pos: QPoint
    :param pos: 显示位置，默认为鼠标位置
    :type from_widget: QWidget
    :param from_widget: 参考Widget，菜单将显示在其下方
    :type close_callback: callable
    :param close_callback: 关闭回调函数
    :rtype: DockerWarp
    :return: 包装器对象，包含 delete_docker() 方法
    """
```

**使用场景：**
- 右键上下文菜单
- 下拉菜单
- 工具提示窗口

### default_docker()

创建或更新默认窗口。

```python
def default_docker(icon=None, name="Window", title=None, form=tuple(), size=None):
    """
    创建或更新默认窗口
    
    :type icon: str
    :param icon: 窗口图标路径
    :type name: str
    :param name: 窗口名称（用于窗口管理）
    :type title: str
    :param title: 窗口标题，默认使用name
    :type form: QWidget
    :param form: CPForm 表单对象
    :type size: tuple
    :param size: 窗口大小 (width, height)
    """
```

**特点：**
- 如果同名窗口已存在，则更新内容而不创建新窗口
- 窗口会被添加到全局窗口表中进行管理
- 最常用的窗口创建方式

### middle_docker()

创建居中显示的窗口。

```python
def middle_docker(icon=None, name="Window", title=None, form=tuple(), size=None):
    """
    创建居中显示窗口
    
    :type icon: str
    :param icon: 窗口图标路径
    :type name: str
    :param name: 窗口名称
    :type title: str
    :param title: 窗口标题
    :type form: QWidget
    :param form: CPForm 表单对象
    :type size: tuple
    :param size: 窗口大小
    """
```

**注意：** <div style="color: yellow">该功能已弃用，建议使用 `default_docker()` 替代。</div>

### scalable_view_docker()

创建可缩放视图窗口。

```python
def scalable_view_docker(icon=None, name="Window", title=None, form=tuple(), size=None,
                        min_scale=0.2, max_scale=5.0, scale_factor=1.2):
    """
    创建可缩放视图窗口
    
    :type icon: str
    :param icon: 窗口图标路径
    :type name: str
    :param name: 窗口名称
    :type title: str
    :param title: 窗口标题
    :type form: QWidget
    :param form: CPForm 表单对象
    :type size: tuple
    :param size: 窗口大小
    :type min_scale: float
    :param min_scale: 最小缩放比例
    :type max_scale: float
    :param max_scale: 最大缩放比例
    :type scale_factor: float
    :param scale_factor: 缩放因子
    """
```

**注意：** <div style="color: yellow">此功能处于测试阶段，可能存在一些问题。</div>

### widget_docker()

创建Widget容器。

```python
def widget_docker(form=tuple(), parent=None):
    """
    创建Widget容器
    
    :type form: QWidget
    :param form: CPForm 表单对象
    :type parent: QWidget
    :param parent: 父窗口
    :rtype: WidgetDocker
    :return: Widget容器实例
    """
```

## 窗口管理函数

### get_docker()

获取指定名称的窗口实例。

```python
def get_docker(name, default=None):
    """
    获取窗口实例
    
    :type name: str
    :param name: 窗口名称
    :param default: 默认返回值
    :return: 窗口实例或默认值
    """
```

### close_docker()

关闭指定窗口。

```python
def close_docker(name="Window"):
    """
    关闭指定窗口
    
    :type name: str
    :param name: 窗口名称
    :raises CPMelFormException: 当窗口不存在时抛出异常
    """
```

### delete_docker()

删除指定窗口。

```python
def delete_docker(name="Window"):
    """
    删除指定窗口（关闭并从内存中移除）
    
    :type name: str
    :param name: 窗口名称
    :raises CPMelFormException: 当窗口不存在时抛出异常
    """
```

### quit_dialog_docker()

关闭当前活动的对话框。

```python
def quit_dialog_docker():
    """
    关闭当前活动的模态对话框
    """
```
