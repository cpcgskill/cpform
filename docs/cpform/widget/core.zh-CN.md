# cpform.widget.core 参考

`cpform.widget.core` 模块提供声明式UI组件，包括基础控件、布局容器、按钮、输入框等。所有组件都支持统一的样式主题和数据读取接口。

<div style="display: flex; justify-content: space-between;">
  <div>
    <a href="./core.en-US.md">English</a> | <a href="./core.zh-CN.md">中文</a>
  </div>
</div>

## 目录

- [基础组件](#基础组件)
- [文本组件](#文本组件)
- [输入组件](#输入组件)
- [按钮组件](#按钮组件)
- [布局组件](#布局组件)
- [容器组件](#容器组件)
- [交互组件](#交互组件)
- [快速参考](#快速参考)

## 基础组件

### Widget

所有CPForm组件的基类，提供通用的鼠标事件处理和数据接口。

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

**参数：**
- `left_clicked_callback` (callable): 左键点击回调
- `right_clicked_callback` (callable): 右键点击回调
- `min_width/min_height` (int): 最小宽度/高度
- `max_width/max_height` (int): 最大宽度/高度
- `fixed_width/fixed_height` (int): 固定宽度/高度

### Warp / WarpWidget

包装器组件，用于包装其他组件。

```python
def Warp(child, **kwargs):
    """包装子组件"""
```

### Background / BackgroundWidget

带背景的容器组件。

```python
def Background(child, color=config_manager.BackgroundColor, round_corners=config_manager.RoundCornersLevel3, style='Rounded', **kwargs):
    """
    创建带背景的容器
    
    :param child: 子组件
    :param color: 背景颜色
    :param round_corners: 圆角大小
    :param style: 'Rounded' | 'Capsule'， 圆角|胶囊
    """
```

### ToggleWidget

可切换内容的通用容器。

```python
def ToggleWidget(widget=None, **kwargs):
    """可切换的容器组件"""
    
# 方法
def toggle_to(widget):
    """切换到指定组件"""
```

## 文本组件

### Label / LabelWidget

文本标签组件。

```python
def Label(text='', word_wrap=False, font_size=None, align=None, text_color=config_manager.NormalTextColor, **kwargs):
    """
    文本标签
    
    :param text: 显示文本
    :param word_wrap: 是否自动换行
    :param font_size: 字体大小
    :param align: 对齐方式 'left'|'center'|'right'
    :param text_color: 文本颜色
    """
```

### 标题组件

```python
def H1(text='', **kwargs):  # 72px
def H2(text='', **kwargs):  # 59px  
def H3(text='', **kwargs):  # 47px
def H4(text='', **kwargs):  # 36px
def H5(text='', **kwargs):  # 27px
def H6(text='', **kwargs):  # 19px
```

### Help / HelpWidget

帮助文本组件，支持自动换行。

```python
def Help(text='', **kwargs):
    """帮助文本组件"""
```

## 输入组件

### LineEdit / LineEditWidget

单行文本输入框。

```python
def LineEdit(text='', is_encrypt=False, placeholder_text='', tool_tip='', 
             return_pressed_callback=None, validator=None, **kwargs):
    """
    单行文本输入
    
    :param text: 初始文本
    :param is_encrypt: 是否加密显示（密码输入）
    :param placeholder_text: 占位符文本
    :param tool_tip: 工具提示
    :param return_pressed_callback: 回车键回调
    :param validator: 验证器（QValidator或正则表达式）
    """
```

**方法：**
- `set_text(text)`: 设置文本
- `get_text()`: 获取文本
- `read_data()`: 返回 [text]

### 特殊输入框

```python
def IntegerLineEdit(*args, **kwargs):
    """整数输入框，自动验证整数格式"""
    
def FloatLineEdit(*args, **kwargs):
    """浮点数输入框，自动验证浮点数格式"""
    
def EmailLineEdit(*args, **kwargs):
    """邮箱输入框，自动验证邮箱格式"""
```

### 滑块组件

```python
def IntSlider(min=0, max=100, default=0, **kwargs):
    """
    整数滑块
    
    :param min: 最小值
    :param max: 最大值  
    :param default: 默认值
    """

def FloatSlider(min=0, max=1, default=0, **kwargs):
    """浮点数滑块"""
```

### CheckBox / CheckBoxWidget

复选框组件。

```python
def CheckBox(info="", default_state=False, update_func=None, **kwargs):
    """
    复选框
    
    :param info: 显示文本
    :param default_state: 默认选中状态
    :param update_func: 状态变化回调
    """
```

**方法：**
- `set_state(state)`: 设置状态
- `state()`: 获取状态
- `read_data()`: 返回 [bool]

## 按钮组件

### Button / ButtonWidget

基础按钮组件。

```python
def Button(text='', icon=None, icon_size=None, func=None, color=None, text_color=None, **kwargs):
    """
    基础按钮
    
    :param text: 按钮文本
    :param icon: 图标名称（来自feather图标集）
    :param icon_size: 图标大小
    :param func: 点击回调函数
    :param color: 背景颜色
    :param text_color: 文本颜色
    """
```

### 预设样式按钮

```python
def PrimaryButton(**kwargs):    # 主要按钮（蓝色）
def AttentionButton(**kwargs): # 注意按钮（亮蓝色）
def SuccessButton(**kwargs):   # 成功按钮（绿色）
def WarningButton(**kwargs):   # 警告按钮（黄色）
def ErrorButton(**kwargs):     # 错误按钮（红色）
def NormalButton(**kwargs):    # 普通按钮（灰色）
```

## 布局组件

### HBoxLayout

水平布局容器。

```python
def HBoxLayout(childs, margins=5, spacing=config_manager.Spacing, align=None, **kwargs):
    """
    水平布局
    
    :param childs: 子组件列表
    :param margins: 边距 (int或[left,top,right,bottom])
    :param spacing: 组件间距
    :param align: 对齐方式
    """
```

### VBoxLayout

垂直布局容器。

```python
def VBoxLayout(childs, margins=5, spacing=config_manager.Spacing, align=None, **kwargs):
    """垂直布局
    
    :param childs: 子组件列表
    :param margins: 边距 (int或[left,top,right,bottom])
    :param spacing: 组件间距
    :param align: 对齐方式
    """
```

### FormLayout

表单布局容器。

```python
def FormLayout(childs, margins=5, spacing=config_manager.Spacing, align=None, **kwargs):
    """
    表单布局
    
    :param childs: [label1, widget1, label2, widget2, ...] 交替的标签和组件
    :param margins: 边距 (int或[left,top,right,bottom])
    :param spacing: 组件间距
    :param align: 对齐方式
    """
```

## 容器组件

### ScrollArea / ScrollAreaWidget

滚动区域容器。

```python
def ScrollArea(widget, hide_scroll_bar=False, **kwargs):
    """
    滚动容器
    
    :param widget: 内容组件
    :param hide_scroll_bar: 是否隐藏滚动条
    """
```

### Collapse / CollapseWidget

可折叠容器。

```python
def Collapse(body, text='', default_state=False, **kwargs):
    """
    可折叠容器
    
    :param body: 主体内容组件
    :param text: 折叠标题
    :param default_state: 默认状态（False=折叠, True=展开）
    """
```

## 交互组件

### SubmitWidget

表单提交容器，自动收集子组件数据。

```python
def SubmitWidget(form=tuple(), func=lambda *args: 0, doit_text="Apply", 
                 margins=5, spacing=config_manager.Spacing, align=None, **kwargs):
    """
    表单提交容器
    
    :param form: 表单组件列表
    :param func: 提交时调用的函数，传入所有组件的数据
    :param doit_text: 提交按钮文本
    :param margins: 边距设置
    :param spacing: 组件间距
    :param align: 对齐方式
    """
```

**方法：**
- `doit_value()`: 获取所有子组件的数据
- `doit()`: 触发提交操作

## 快速参考

### 组件分类

| 类型 | 组件 | 用途 |
|------|------|------|
| **基础** | `Widget`, `Warp`, `Background`, `ToggleWidget` | 基础容器和包装 |
| **文本** | `Label`, `H1`~`H6`, `Help` | 文本显示 |
| **输入** | `LineEdit`, `IntegerLineEdit`, `FloatLineEdit`, `EmailLineEdit` | 文本输入 |
| **滑块** | `IntSlider`, `FloatSlider` | 数值选择 |
| **选择** | `CheckBox` | 布尔选择 |
| **按钮** | `Button`, `PrimaryButton`, `SuccessButton` 等 | 操作触发 |
| **布局** | `HBoxLayout`, `VBoxLayout`, `FormLayout` | 组件排列 |
| **容器** | `ScrollArea`, `Collapse`, `SubmitWidget` | 内容组织 |

### 常用参数

**尺寸控制：**
- `min_width`, `min_height`: 最小尺寸
- `max_width`, `max_height`: 最大尺寸
- `fixed_width`, `fixed_height`: 固定尺寸

**布局参数：**
- `margins`: 边距，可为整数或[left,top,right,bottom]
- `spacing`: 组件间距
- `align`: 对齐方式 ('left', 'center', 'right', 'top', 'bottom')

**回调函数：**
- `func`: 按钮点击回调
- `update_func`: 状态变化回调
- `return_pressed_callback`: 回车键回调
- `left_clicked_callback`: 左键点击回调
- `right_clicked_callback`: 右键点击回调

### 数据接口

所有组件都实现 `read_data()` 方法：

```python
# 输入组件返回输入值
line_edit.read_data()  # ['text']
check_box.read_data()  # [True/False]
slider.read_data()     # [number]

# 容器组件返回子组件数据的生成器
layout.read_data()     # 生成器，遍历所有子组件数据
```

### 样式自定义

```python
# 自定义颜色
Button(color='#ff0000', text_color='#ffffff')
Background(color='#333333')

# 自定义字体
Label(font_size=16, text_color='#666666')

# 自定义圆角
Background(round_corners=10, style='Capsule')
```

### 常用组合

```python
# 表单行
FormLayout([
    '用户名:', LineEdit(),
    '密码:', LineEdit(is_encrypt=True),
])

# 按钮组
HBoxLayout([
    PrimaryButton(text='确定', func=confirm),
    NormalButton(text='取消', func=cancel),
])

# 设置面板
Collapse(
    VBoxLayout([
        CheckBox('启用功能'),
        IntSlider(0, 100, 50),
        LineEdit(placeholder_text='输入路径'),
    ]),
    text='高级设置'
)
```