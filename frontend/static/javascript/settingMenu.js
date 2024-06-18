//parsing and activating themes

function Change_editor_theme(theme_name){
  console.log("Changing theme to:"+theme_name)
  fetch('/node/monaco-themes/themes/'+theme_name)
  .then(response=>response.json())
  .then(response_theme=>{
    console.log(response_theme)
    monaco.editor.defineTheme('customtheme',response_theme)
    monaco.editor.setTheme('customtheme')
  })
  .catch(error=>console.log(error))
} 
