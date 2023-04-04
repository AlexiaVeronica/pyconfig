# pyconfig

## Function: A simple configuration file management class that supports storing and retrieving multi-level configuration information.

  - `init(self, file_path):` Initialization function takes a file path, creates an empty file if it does not exist, and
  stores the configuration information in the class property 'config'.
  - `_load_config(self) -> dict:` Loads configuration information from a file and returns a dictionary.
  - `_save_config(self):` Saves the configuration information to a file.
  - `get_value(self, key):` Retrieves the corresponding configuration information based on the passed key value.
  - `set_value(self, key, value):` Sets the configuration information based on the passed key value and value, and saves it
    to the file.
  - `add_value(self, key, value):` Similar to set_value, but creates a new level if a certain level does not exist and saves
    the value to the final level.
  - `delete_value(self, key):` Deletes the corresponding configuration information based on the passed key value and saves
    it to the file.

## function: 一个简单的配置文件管理类，支持多层级配置信息的存储和读取。

- __init__(self, file_path)：初始化函数，传入一个文件路径，如果该文件不存在则创建空文件，并将配置信息存储在类属性 config 中。
- _load_config(self) -> dict：从文件中加载配置信息并返回一个字典。
- _save_config(self)：将配置信息保存到文件中。
- get_value(self, key)：根据传入的键值获取对应的配置信息。
- set_value(self, key, value)：根据传入的键值和值设置配置信息，并将其保存到文件中。
- add_value(self, key, value)：类似于 set_value，但是如果某一层级不存在，则新建该层级，并将值保存到最终层级。
- delete_value(self, key)：根据传入的键值删除对应的配置信息，并将其保存到文件中。