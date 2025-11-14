try:
    import moviepy
    print("✅ 成功匯入 moviepy")
    print("moviepy 模組屬性與方法：")
    print(dir(moviepy))
    print("==============================================================")

    import moviepy.video
    print("✅ 成功匯入 moviepy.video")
    print("moviepy.video 模組屬性與方法：")
    print(dir(moviepy.video))
    print("==============================================================")

    import moviepy.audio as mp
    print("✅ 成功匯入 moviepy.audio")
    print("moviepy.audio 模組屬性與方法：")
    print(dir(moviepy.audio))
    print("==============================================================")
    
    print("📘 moviepy.editor 模組的文檔說明：")
    help(mp)
    print("==============================================================")

except ImportError as e:
    print(f"❌ 匯入失敗：{e}")
except Exception as e:
    print(f"⚠️ 執行錯誤：{e}")