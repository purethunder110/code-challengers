
let GlobalEditorObject= null

document.addEventListener('DOMContentLoaded',(event)=>{
    /*
    //for codemirror
    var editor = CodeMirror.fromTextArea(document.getElementById('code-editor'), {
        lineNumbers: true,
        mode: "javascript",
        theme: "material",
        lineWrapping:true,
        gutters:["CodeMirror-lint-makers"],
        lint:true
    });
    */
    //for vseditor
    require.config({ paths: { vs: '/node/monaco-editor/min/vs' } });

    require(['vs/editor/editor.main'], function () {
        var editor = monaco.editor.create(document.getElementById('code-editor'), {
        value: ['console.log("hello world")'].join('\n'),
        language: 'javascript',
        minimap:{"enabled": false},
        theme:"vs-dark"
        });
        GlobalEditorObject=editor
    });
});




document.getElementById("Run_code").addEventListener('click',function(){
    var source_code=GlobalEditorObject.getValue()
    var data={
        "platform":"python",
        "code":source_code
    }
    axios.post("/api/code-reciever/",data)
    .then(response=>console.log(response))
    .catch(error=>console.log(error))
})