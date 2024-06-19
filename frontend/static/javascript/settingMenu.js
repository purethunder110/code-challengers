//parsing and activating themes

function Change_editor_theme(theme_name){
  console.log("Changing theme to:"+theme_name)
  fetch('/node/monaco-themes/themes/'+theme_name)
  .then(response=>response.json())
  .then(response_theme=>{
    monaco.editor.defineTheme('customtheme',response_theme)
    monaco.editor.setTheme('customtheme')
    //saving theme for future
    window.localStorage.setItem("editor-theme",theme_name)
  })
  .catch(error=>console.log(error))
} 

function Change_start_theme(theme_name,monaco){
  fetch('/node/monaco-themes/themes/'+theme_name)
  .then(response=>response.json())
  .then(response_theme=>{
    monaco.editor.defineTheme('customtheme',response_theme)
    monaco.editor.setTheme('customtheme')
    //saving theme for future
    window.localStorage.setItem("editor-theme",theme_name)
  })
  .catch(error=>console.log(error))
}



function change_theme(uitheme){
  console.log(uitheme)
  window.localStorage.setItem("theme",uitheme)
  window.localStorage.setItem("ui-theme",uitheme)
}
