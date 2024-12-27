import moviepy

# 列出 moviepy 模組中的所有属性和方法
print("列出 moviepy 模組中的所有属性和方法")
print(dir(moviepy))
print("==============================================================")

# 列出 moviepy.video 模組中的所有屬性和方法
import moviepy.video as mv
print("列出 moviepy.video 模組中的所有屬性和方法")
print(dir(mv))
print("==============================================================")

# 列出 moviepy.audio 模組中的所有屬性和方法
import moviepy.audio as ma
print("列出 moviepy.audio 模組中的所有屬性和方法")
print(dir(ma))
print("==============================================================")

# 列出 moviepy.editor 模組中的所有属性和方法
import moviepy.editor as mp
print("列出 moviepy.editor 模組中的所有属性和方法")
print(dir(mp))
print("==============================================================")


# 列出 moviepy.editor 模組中的所有屬性和方法
try:
    import moviepy.editor as mp
    print("\nmoviepy.editor 模組中的屬性和方法：")
    print(dir(mp)) 
except ImportError as e:
    print(f"無法導入 moviepy.editor 模組：{e}")
print("==============================================================")


# 顯示 moviepy.editor 模組的文檔字符串
# 可以使用 help() 函數來查看模組的文檔字符串, 其中包含模組中的類和函數說明
print("顯示 moviepy.editor 模組的文檔字符串")
help(mp)
print("==============================================================")
