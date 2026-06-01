from pathlib import Path
p = Path(r'c:/Users/RajSuratia/Downloads/mine/RevoltGroup/revolt-group-website.html')
text = p.read_text(encoding='utf-8', errors='replace')
text = text.replace('\r\n', '\n')
start = text.index('<div class="about-image-wrap">')
start2 = text.index('\n      <div>\n          <img src="data:image', start)
end_marker = '\n      <div>\n        <div class="tag">About Revolt Group</div>'
end = text.index(end_marker, start2)
fixed = text[:start2] + '\n      </div>\n\n      <div>\n        <div class="tag">About Revolt Group</div>' + text[end+len(end_marker):]
old_css = '  /* Ensure logos or photos fit neatly inside the about box */\n  .about-img-main img,\n  .about-img-main svg {\n    max-width: 80%;\n    max-height: 80%;\n    width: auto;\n    height: auto;\n    display: block;\n    object-fit: contain;\n  }\n'
new_css = '  /* Ensure logos or photos fit neatly inside the about box */\n  .about-img-main img,\n  .about-img-main svg {\n    max-width: 100%;\n    max-height: 100%;\n    width: 100%;\n    height: 100%;\n    display: block;\n    object-fit: cover;\n  }\n'
fixed = fixed.replace(old_css, new_css, 1)
p.write_text(fixed.replace('\n', '\r\n'), encoding='utf-8')
print('fixed', start2, '->', end)
